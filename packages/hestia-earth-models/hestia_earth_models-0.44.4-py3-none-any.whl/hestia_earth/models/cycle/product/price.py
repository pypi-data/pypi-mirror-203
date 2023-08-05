"""
Product Price

Sets the `price` of products to `0` in specific conditions: if the `economicValueShare` is `0`, or for `excreta`.
"""
from hestia_earth.utils.tools import non_empty_list

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.currency import DEFAULT_CURRENCY
from .utils import lookup_share
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{"@type": "Product"}]
    }
}
RETURNS = {
    "Product": [{
        "price": ""
    }]
}
MODEL_KEY = 'price'


def _product(product: dict, value: float):
    # currency is required, but do not override if present
    # currency in lookup table is set to USD
    return {'currency': DEFAULT_CURRENCY, **product, MODEL_KEY: value}


def _should_run_product_by_share_0(cycle: dict, product: dict):
    term_id = product.get('term', {}).get('@id')
    share = lookup_share(MODEL_KEY, product)
    share_is_0 = share is not None and share == 0

    logRequirements(cycle, model=MODEL, term=term_id, key=MODEL_KEY, by='economicValueShare',
                    share_is_0=share_is_0)

    should_run = all([share_is_0])
    logShouldRun(cycle, MODEL, term_id, should_run, key=MODEL_KEY, by='economicValueShare')
    return should_run


def run(cycle: dict):
    return non_empty_list([
        (
            _product(p, 0) if _should_run_product_by_share_0(cycle, p) else None
        ) for p in cycle.get('products', [])
    ])
