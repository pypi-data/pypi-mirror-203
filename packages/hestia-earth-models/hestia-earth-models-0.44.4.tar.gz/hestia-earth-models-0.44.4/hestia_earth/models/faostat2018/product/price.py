"""
Product Price

Calculates the price of `crop` and `liveAnimal` using FAOSTAT data.
"""
from hestia_earth.schema import TermTermType
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.lookup import get_table_value, column_name, download_lookup, extract_grouped_data
from hestia_earth.utils.tools import non_empty_list, safe_parse_float, safe_parse_date

from hestia_earth.models.log import debugMissingLookup, debugValues, logRequirements, logShouldRun
from hestia_earth.models.utils.constant import Units
from hestia_earth.models.utils.currency import DEFAULT_CURRENCY
from hestia_earth.models.utils.crop import FAOSTAT_PRODUCTION_LOOKUP_COLUMN, get_crop_grouping_faostat_production
from hestia_earth.models.utils.animalProduct import (
    FAO_LOOKUP_COLUMN, get_animalProduct_grouping_fao, get_animalProduct_lookup_value
)
from hestia_earth.models.utils.product import convert_product_to_unit
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{
            "@type": "Product",
            "term.termType": ["crop", "animalProduct", "liveAnimal"]
        }],
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"}
        }
    }
}
RETURNS = {
    "Product": [{
        "price": ""
    }]
}
LOOKUPS = {
    "@doc": "Depending on the primary product [termType](https://hestia.earth/schema/Product#term)",
    "crop": "cropGroupingFaostatProduction",
    "region-crop-cropGroupingFaostatProduction-price": "use value from above",
    "liveAnimal": "primaryMeatProductFAO",
    "animalProduct": ["animalProductGroupingFAOEquivalent", "animalProductGroupingFAO", "liveAnimal"],
    "region-animalProduct-animalProductGroupingFAO-price": "use value from above",
    "region-animalProduct-animalProductGroupingFAO-averageColdCarcassWeight": "use value from above"
}
MODEL_KEY = 'price'
LOOKUP_NAME = {
    TermTermType.CROP.value: f"region-{TermTermType.CROP.value}-{FAOSTAT_PRODUCTION_LOOKUP_COLUMN}-price.csv",
    TermTermType.ANIMALPRODUCT.value: f"region-{TermTermType.ANIMALPRODUCT.value}-{FAO_LOOKUP_COLUMN}-price.csv"
}
LOOKUP_GROUPING = {
    TermTermType.CROP.value: get_crop_grouping_faostat_production,
    TermTermType.ANIMALPRODUCT.value: get_animalProduct_grouping_fao
}
LOOKUP_WEIGHT = 'region-animalProduct-animalProductGroupingFAO-averageColdCarcassWeight.csv'


def _term_grouping(term: dict): return LOOKUP_GROUPING.get(term.get('termType'), lambda *_: None)(MODEL, term)


def _lookup_data(
    term_id: str, grouping: str, country_id: str, year: int, term_type: str = None, lookup_name: str = None
):
    lookup_name = lookup_name or LOOKUP_NAME.get(term_type)
    lookup = download_lookup(lookup_name)
    data = get_table_value(lookup, 'termid', country_id, column_name(grouping))
    debugMissingLookup(lookup_name, 'termid', country_id, grouping, data,
                       model=MODEL, term=term_id, key=MODEL_KEY)
    price = extract_grouped_data(data, str(year)) if year else extract_grouped_data(data, 'Average_price_per_tonne')
    return safe_parse_float(price, None)


def _product(product: dict, value: float):
    # currency is required, but do not override if present
    # currency in lookup table is set to USD
    return {'currency': DEFAULT_CURRENCY, **product, MODEL_KEY: round(value, 4)}


def _get_animalProductId(term_id: str):
    lookup_name = 'liveAnimal.csv'
    lookup = download_lookup(lookup_name)
    value = get_table_value(lookup, 'termid', term_id, column_name(LOOKUPS.get('liveAnimal')))
    debugMissingLookup(lookup_name, 'termid', term_id, LOOKUPS.get('liveAnimal'), value,
                       model=MODEL, term=term_id, key=MODEL_KEY)
    return value


def _get_liveAnimal_lookup_values(cycle: dict, product: dict, country_id: str, year: int = None):
    term_id = product.get('term', {}).get('@id')
    animal_product = _get_animalProductId(term_id)
    groupingFAO = get_animalProduct_lookup_value(MODEL, animal_product, FAO_LOOKUP_COLUMN) if animal_product else None

    # one live animal can be linked to many animal product, hence go one by one until we have a match
    if groupingFAO:
        average_carcass_weight = _lookup_data(animal_product, groupingFAO, country_id, year, lookup_name=LOOKUP_WEIGHT)
        price = _lookup_data(term_id, groupingFAO, country_id, year, term_type=TermTermType.ANIMALPRODUCT.value)
        debugValues(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by='liveAnimal',
                    animal_product=animal_product,
                    groupingFAO=groupingFAO,
                    average_carcass_weight_hg=average_carcass_weight,
                    price_per_ton=price)
        if price and average_carcass_weight:
            # price is per 1000kg, divide by 1000 to go back to USD/kg
            # average_carcass_weight is in hg, divide by 10 to go back to kg
            return (animal_product, price / 1000, average_carcass_weight / 10)
    return (None, None, None)


def _run_by_liveAnimal(cycle: dict, product: dict, country_id: str, year: int = None):
    term_id = product.get('term', {}).get('@id')
    animal_product, price, carcass_weight = _get_liveAnimal_lookup_values(cycle, product, country_id, year)

    animal_product = download_hestia(animal_product)
    price_per_carcass_weight = convert_product_to_unit({
        'term': animal_product,
        'value': [price]
    }, Units.KG_COLD_CARCASS_WEIGHT) if price else None
    should_run = all([price_per_carcass_weight, carcass_weight])
    value = price_per_carcass_weight * carcass_weight if should_run else None

    logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by='liveAnimal',
                    price_from_lookup=price,
                    carcass_weight_kg=carcass_weight,
                    price_per_carcass_weight=price_per_carcass_weight,
                    price=value)

    logShouldRun(cycle, MODEL, term_id, should_run, key=MODEL_KEY, by='liveAnimal')

    return _product(product, value) if value is not None else None


def _should_run_liveAnimal(product: dict):
    return product.get('term', {}).get('termType') == TermTermType.LIVEANIMAL.value


def _run_by_country(cycle: dict, product: dict, country_id: str, year: int = None):
    product_term = product.get('term', {})
    term_id = product_term.get('@id')
    term_type = product_term.get('termType')

    has_yield = len(product.get('value', [])) > 0
    not_already_set = MODEL_KEY not in product.keys()

    # get the grouping used in region lookup
    grouping = _term_grouping(product_term) or None

    should_run = all([not_already_set, has_yield, grouping])
    value = _lookup_data(term_id, grouping, country_id, year, term_type=term_type) if should_run else None

    logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by='country',
                    has_yield=has_yield,
                    not_already_set=not_already_set,
                    groupingFAO=grouping,
                    price_per_ton=value)

    logShouldRun(cycle, MODEL, term_id, should_run, key=MODEL_KEY, by='country')

    # divide by 1000 to convert price per tonne to kg
    return _product(product, value / 1000) if value is not None else None


def _should_run(cycle: dict):
    country_id = cycle.get('site', {}).get('country', {}).get('@id')

    logRequirements(cycle, model=MODEL, key=MODEL_KEY,
                    country_id=country_id)

    should_run = all([country_id])
    logShouldRun(cycle, MODEL, None, should_run, key=MODEL_KEY)
    return should_run, country_id


def run(cycle: dict):
    should_run_by_country, country_id = _should_run(cycle)
    end_date = safe_parse_date(cycle.get('endDate'))
    year = end_date.year if end_date else None
    return non_empty_list([
        (
            (
                (_run_by_liveAnimal(cycle, p, country_id, year) if _should_run_liveAnimal(p) else None)
                or _run_by_country(cycle, p, country_id, year)
            ) if should_run_by_country else None
        ) for p in cycle.get('products', [])
    ])
