"""
Product Economic Value Share

This model quantifies the relative economic value share of each marketable Product in a Cycle.
Marketable Products are all Products in the Glossary with the exception of crop residue not sold.

It works in the following order:
1. If revenue data are provided for all marketable products,
the `economicValueShare` is directly calculated as the share of revenue of each Product;
2. If the primary product is a crop and it is the only crop Product,
`economicValueShare` is assigned based on a lookup table containing typical global average economic value shares
drawn from [Poore & Nemecek (2018)](https://science.sciencemag.org/content/360/6392/987).
"""
from hestia_earth.schema import TermTermType
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.cycle import unique_currencies
from .utils import lookup_share
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{
            "@type": "Product",
            "value": "",
            "economicValueShare": "",
            "revenue": "",
            "currency": ""
        }],
        "optional": {
            "completeness.products": ""
        }
    }
}
RETURNS = {
    "Product": [{
        "economicValueShare": ""
    }]
}
LOOKUPS = {
    "@doc": "Depending on the primary product [termType](https://hestia.earth/schema/Product#term)",
    "crop": "global_economic_value_share",
    "excreta": "global_economic_value_share"
}
MODEL_KEY = 'economicValueShare'
MAX_VALUE = 100.5
MIN_VALUE = 99.5
MIN_COMPLETE_VALUE = 80  # when the products are complete lower the min threshold to 80% and rescale


def _product(product: dict, value: float):
    return {**product, MODEL_KEY: value}


def _is_complete(cycle: dict): return cycle.get('completeness', {}).get('products', False)


def _no_yield(product): return list_sum(product.get('value', [-1]), -1) == 0


def _total_revenue(products: list): return sum([p.get(MODEL_KEY, 0) for p in products])


def _product_with_value(product: dict):
    value = product.get(MODEL_KEY, lookup_share(MODEL_KEY, product))
    return {**product, MODEL_KEY: value} if value is not None else product


def _rescale_value(products: list, total: float):
    return list(map(lambda p: {**p, MODEL_KEY: p.get(MODEL_KEY) * 100 / total}, products))


def _run_by_default(cycle: dict, products: list):
    run_by = 'default'
    is_complete = _is_complete(cycle)
    products = list(map(_product_with_value, products))
    # remove results where lookup share was not found
    results = list(filter(lambda p: p.get(MODEL_KEY) is not None, products))
    # only return list if the new total of evs is not above threshold
    total_revenue = _total_revenue(results)
    below_threshold = total_revenue <= MAX_VALUE
    should_rescale = is_complete and MIN_COMPLETE_VALUE <= total_revenue <= MAX_VALUE
    above_threshold = True if should_rescale else total_revenue >= MIN_VALUE if is_complete else True
    results = _rescale_value(results, total_revenue) if should_rescale else results

    should_run = all([below_threshold, above_threshold])

    for p in products:
        term_id = p.get('term', {}).get('@id')
        p_should_run = all([should_run, find_term_match(results, term_id)])
        logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by=run_by,
                        below_threshold=below_threshold,
                        above_threshold=above_threshold,
                        total_revenue=total_revenue)
        logShouldRun(cycle, MODEL, term_id, p_should_run, key=MODEL_KEY, by=run_by)

    return results if should_run else []


def _run_by_revenue(products: list):
    total_revenue = sum([p.get('revenue', 0) for p in products])
    return list(map(
        lambda p: _product(p, p.get('revenue') / total_revenue * 100) if p.get('revenue', 0) > 0 else p, products
    ))


def _should_run_by_revenue(cycle: dict, products: list):
    run_by = 'revenue'
    is_complete = _is_complete(cycle)
    total_value = _total_revenue(products)
    below_threshold = total_value < MAX_VALUE
    # ignore products with no yield
    products = list(filter(lambda p: not _no_yield(p), products))
    currencies = unique_currencies(cycle)
    same_currencies = len(currencies) < 2
    all_with_revenue = all([p.get('revenue', -1) >= 0 for p in products])

    should_run = all([is_complete, below_threshold, all_with_revenue, same_currencies])
    for p in products:
        term_id = p.get('term', {}).get('@id')
        logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by=run_by,
                        is_complete=is_complete,
                        total_value=total_value,
                        below_threshold=below_threshold,
                        all_with_revenue=all_with_revenue,
                        currencies=';'.join(currencies),
                        same_currencies=same_currencies)

        logShouldRun(cycle, MODEL, term_id, should_run, key=MODEL_KEY, by=run_by)
    return should_run


def _run_single_missing_evs(products: list):
    total_value = _total_revenue(products)
    return list(map(lambda p: _product(p, 100 - total_value) if p.get(MODEL_KEY) is None else p, products))


def _should_run_single_missing_evs(cycle: dict, products: list):
    run_by = '1-missing-evs'
    is_complete = _is_complete(cycle)
    total_value = _total_revenue(products)
    # ignore products with no yield
    products = list(filter(lambda p: not _no_yield(p), products))
    missing_values = [p for p in products if p.get(MODEL_KEY) is None]
    single_missing_value = len(missing_values) == 1
    below_threshold = total_value < MAX_VALUE
    term_id = missing_values[0].get('term', {}).get('@id') if single_missing_value else None

    logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by=run_by,
                    is_complete=is_complete,
                    total_value=total_value,
                    below_threshold=below_threshold,
                    single_missing_value=single_missing_value)

    should_run = all([is_complete, below_threshold, single_missing_value])
    logShouldRun(cycle, MODEL, term_id, should_run, key=MODEL_KEY, by=run_by)
    return should_run


def _should_run_no_value(cycle: dict, product: dict):
    run_by = '0-value'
    term_id = product.get('term', {}).get('@id')
    value_0 = _no_yield(product)
    revenue_0 = product.get('revenue', -1) == 0

    logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by=run_by,
                    value_0=value_0,
                    revenue_0=revenue_0)

    should_run = any([value_0, revenue_0])
    logShouldRun(cycle, MODEL, term_id, should_run, key=MODEL_KEY, by=run_by)
    return should_run


def _should_have_evs(product: dict):
    term_type = product.get('term', {}).get('termType')
    return term_type not in [
        TermTermType.CROPRESIDUE.value,
        TermTermType.EXCRETA.value
    ]


def run(cycle: dict):
    products = cycle.get('products', [])
    # skip any product that will never has value
    products = list(filter(_should_have_evs, products))
    products = list(map(lambda p: _product(p, 0) if _should_run_no_value(cycle, p) else p, products))
    return (
        _run_single_missing_evs(products) if _should_run_single_missing_evs(cycle, products) else
        _run_by_revenue(products) if _should_run_by_revenue(cycle, products) else
        _run_by_default(cycle, products)
    )
