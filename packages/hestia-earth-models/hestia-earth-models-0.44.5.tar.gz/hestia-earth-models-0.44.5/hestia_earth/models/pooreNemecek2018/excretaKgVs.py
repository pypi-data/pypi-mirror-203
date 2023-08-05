"""
Excreta (kg VS)

This model calculates the Excreta (kg VS) from the products as described in
[Poore & Nemecek (2018)](https://science.sciencemag.org/content/360/6392/987).
The model computes it as the balance between the carbon in the inputs plus the carbon produced in the pond
minus the carbon contained in the primary product.
If the mass balance fails
(i.e. [animal feed](https://hestia.earth/schema/Completeness#animalFeed) is not complete, see requirements below),
the fomula is = total excreta as N / [Volatile solids content](https://hestia.earth/term/volatileSolidsContent).
"""
from hestia_earth.schema import ProductStatsDefinition, SiteSiteType, TermTermType
from hestia_earth.utils.model import find_primary_product, find_term_match
from hestia_earth.utils.tools import list_sum, safe_parse_float

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.term import get_lookup_value
from hestia_earth.models.utils.constant import Units
from hestia_earth.models.utils.property import get_node_property
from hestia_earth.models.utils.product import _new_product
from hestia_earth.models.utils.input import get_feed_carbon
from hestia_earth.models.utils.measurement import most_relevant_measurement_value
from hestia_earth.models.utils.term import get_excreta_terms
from . import MODEL
from .excretaKgN import _get_excreta_n_term

REQUIREMENTS = {
    "Cycle": {
        "or": [
            {
                "completeness.animalFeed": "",
                "completeness.products": "",
                "inputs": [{
                    "@type": "Input",
                    "term.termType": ["crop", "animalProduct", "feedFoodAdditive"],
                    "term.units": "kg",
                    "value": "> 0",
                    "isAnimalFeed": "True",
                    "optional": {
                        "properties": [
                            {"@type": "Property", "value": "", "term.@id": "carbonContent"},
                            {"@type": "Property", "value": "", "term.@id": "energyContentHigherHeatingValue"}
                        ]
                    }
                }],
                "products": [{
                    "@type": "Product",
                    "primary": "True",
                    "value": "",
                    "properties": [{"@type": "Property", "value": "", "term.@id": "carbonContent"}]
                }],
                "practices": [
                    {"@type": "Practice", "value": "", "term.@id": "slaughterAge"},
                    {"@type": "Practice", "value": "", "term.@id": "yieldOfPrimaryAquacultureProductLiveweightPerM2"}
                ],
                "site": {
                    "@type": "Site",
                    "measurements": [{"@type": "Measurement", "value": "", "term.@id": "netPrimaryProduction"}]
                }
            },
            {
                "products": [{
                    "@type": "Product",
                    "primary": "True",
                    "value": "",
                    "term.termType": ["animalProduct", "liveAnimal", "liveAquaticSpecies"]
                }]
            }
        ]
    }
}
RETURNS = {
    "Product": [{
        "value": "",
        "statsDefinition": "modelled"
    }]
}
LOOKUPS = {
    "crop-property": ["carbonContent", "energyContentHigherHeatingValue"],
    "animalProduct": "excretaKgVsTermId",
    "liveAnimal": "excretaKgVsTermId",
    "liveAquaticSpecies": "excretaKgVsTermId"
}
MODEL_KEY = 'excretaKgVs'
MODEL_LOG = '/'.join([MODEL, MODEL_KEY])

Conv_AQ_CLW_CO2CR = 1
Conv_AQ_CLW_CExcr = 0.5
Conv_AQ_OC_OCSed_Marine = 0.55
Conv_AQ_OC_OCSed_Fresh = 0.35


def _product(value: float, excreta: str):
    product = _new_product(excreta, value, MODEL)
    product['statsDefinition'] = ProductStatsDefinition.MODELLED.value
    return product


def _run(mass_balance_items: list, inputs_c: float, term_id: str, alternate_items: list):
    carbonContent, tsy, slaughterAge, aqocsed, npp = mass_balance_items
    excretaKgN, vsc = alternate_items
    value = max(
        inputs_c + (npp * slaughterAge) / (tsy * 1000) - carbonContent - carbonContent * Conv_AQ_CLW_CO2CR,
        carbonContent * Conv_AQ_CLW_CExcr
    ) * aqocsed if all(mass_balance_items) else excretaKgN * vsc / 100
    return [_product(value, term_id)] if value > 0 else []


def _get_carbonContent(cycle: dict):
    primary_prod = find_primary_product(cycle) or {}
    return safe_parse_float(get_lookup_value(primary_prod.get('term', {}), 'carbonContent', model=MODEL)) / 100


def _get_excreta_vs_term(product: dict):
    term = product.get('term', {})
    return get_lookup_value(term, LOOKUPS.get(term.get('termType', TermTermType.ANIMALPRODUCT.value)), model=MODEL)


def _no_excreta_term(products: list):
    term_ids = get_excreta_terms(Units.KG_VS)
    return all([not find_term_match(products, term) for term in term_ids])


def _get_conv_aq_ocsed(siteType: str):
    return Conv_AQ_OC_OCSed_Marine if siteType == SiteSiteType.SEA_OR_OCEAN.value else Conv_AQ_OC_OCSed_Fresh


def _should_run(cycle: dict):
    primary_prod = find_primary_product(cycle) or {}
    excreta_term_id = _get_excreta_vs_term(primary_prod)

    dc = cycle.get('completeness', {})
    is_complete = dc.get('animalFeed', False) and dc.get('products', False)
    carbonContent = _get_carbonContent(cycle)

    products = cycle.get('products', [])
    should_add_product = _no_excreta_term(products)

    inputs = cycle.get('inputs', [])
    inputs_c = get_feed_carbon(cycle, MODEL_LOG, excreta_term_id, inputs)

    practices = cycle.get('practices', [])
    tsy = list_sum(find_term_match(practices, 'yieldOfPrimaryAquacultureProductLiveweightPerM2').get('value', []))
    slaughterAge = list_sum(find_term_match(practices, 'slaughterAge').get('value', []))

    end_date = cycle.get('endDate')
    site = cycle.get('site', {})
    aqocsed = _get_conv_aq_ocsed(site.get('siteType', {}))
    npp = most_relevant_measurement_value(site.get('measurements', []), 'netPrimaryProduction', end_date, 0)

    # we can still run the model with excreta in "kg N" units
    excreta = _get_excreta_n_term(primary_prod)
    excreta_product = find_term_match(products, excreta)
    excretaKgN = list_sum(excreta_product.get('value', [0]))
    vsc = get_node_property(excreta_product, 'volatileSolidsContent').get('value', 0)

    logRequirements(cycle, model=MODEL_LOG, term=excreta_term_id,
                    is_complete=is_complete,
                    aqocsed=aqocsed,
                    inputs_c=inputs_c,
                    carbonContent=carbonContent,
                    yield_of_target_species=tsy,
                    slaughterAge=slaughterAge,
                    netPrimaryProduction=npp,
                    should_add_product=should_add_product,
                    excretaKgN=excretaKgN,
                    volatileSolidsContent=vsc)

    mass_balance_items = [carbonContent, tsy, slaughterAge, aqocsed, npp]
    alternate_items = [excretaKgN, vsc]

    should_run = all([
        excreta_term_id,
        should_add_product,
        any([
            is_complete and all(mass_balance_items),
            all(alternate_items)
        ])
    ])
    # only log if the excreta term does not exist to avoid showing failure when it already exists
    if should_add_product:
        logShouldRun(cycle, MODEL_LOG, excreta_term_id, should_run)
    logShouldRun(cycle, MODEL_LOG, None, should_run)
    return should_run, mass_balance_items, inputs_c, excreta_term_id, alternate_items


def run(cycle: dict):
    should_run, mass_balance_items, inputs_c, term_id, alternate_items = _should_run(cycle)
    return _run(mass_balance_items, inputs_c, term_id, alternate_items) if should_run else []
