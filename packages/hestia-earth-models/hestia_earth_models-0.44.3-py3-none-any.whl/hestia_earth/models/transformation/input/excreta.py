"""
Input Excreta

Copy Cycle (or previous Transformation) `excreta` products into the Transformation inputs if they are missing.
"""
from functools import reduce
from hestia_earth.schema import NodeType, TermTermType
from hestia_earth.utils.model import filter_list_term_type, find_term_match
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logShouldRun
from hestia_earth.models.utils import term_id_prefix
from hestia_earth.models.utils.input import _new_input
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "products": [{"@type": "Product", "value": "", "term.termType": "excreta"}],
        "transformations": [
            {
                "@type": "Transformation",
                "term.termType": "excretaManagement",
                "inputs": [{"@type": "Input", "value": "", "term.termType": "excreta"}]
            }
        ]
    }
}
RETURNS = {
    "Transformation": [{
        "inputs": [{
            "@type": "Input",
            "term.termType": "excreta",
            "value": ""
        }]
    }]
}
MODEL_KEY = 'excreta'
MODEL_LOG = '/'.join([MODEL, 'input', MODEL_KEY])


def _to_input(transformation: dict):
    def new_input(values: tuple):
        product, ratio = values
        data = {**product}
        if 'primary' in data.keys():
            del data['primary']
        logShouldRun(transformation, MODEL_LOG, product.get('term', {}).get('@id'), True)
        return {
            **data,
            **_new_input(product.get('term')),
            'value': [v * ratio for v in product.get('value', [])]
        }
    return new_input


def _group_by_prefix(values: dict, input: dict):
    term_id = input.get('term', {}).get('@id')
    group_id = term_id_prefix(term_id)
    values[group_id] = values.get(group_id, [])
    values[group_id].append(input)
    return values


def _input_ratio(products: list, input: dict):
    term_id = input.get('term', {}).get('@id')
    product = find_term_match(products, term_id)
    product_value = list_sum(product.get('value', 0))
    return list_sum(input.get('value', 0)) / product_value if product and product_value > 0 else None


def _group_missing_products(products: list):
    def group_by(values: list, inputs: list):
        missing_products = [p for p in products if not find_term_match(inputs, p.get('term', {}).get('@id'))]
        ratio = next((_input_ratio(products, i) for i in inputs), None)
        return values + ([(p, ratio) for p in missing_products] if ratio else [])
    return group_by


def _previous_transformation(cycle: dict, transformations: list, transformation: dict):
    term_id = transformation.get('previousTransformationTerm', {}).get('@id')
    return next(
        (v for v in transformations if v.get('term', {}).get('@id') == term_id),
        cycle
    )


def _run_transformation(cycle: dict):
    def run(transformations: list, transformation: dict):
        previous = _previous_transformation(cycle, transformations, transformation)
        products = filter_list_term_type(previous.get('products', []), TermTermType.EXCRETA)
        inputs = transformation.get('inputs', [])
        excreta = filter_list_term_type(transformation.get('inputs'), TermTermType.EXCRETA)
        grouped_inputs = reduce(_group_by_prefix, excreta, {})
        missing_products = reduce(_group_missing_products(products), grouped_inputs.values(), [])
        transformation['inputs'] = inputs + list(map(_to_input(transformation), missing_products))
        return transformations + [transformation]
    return run


def _should_run_transformation(transformation: dict):
    should_run = all([
        transformation.get('term', {}).get('termType') == TermTermType.EXCRETAMANAGEMENT.value
    ])
    logShouldRun(transformation, MODEL_LOG, None, should_run)
    return should_run


def _should_run(cycle: dict):
    node_type = cycle.get('type', cycle.get('@type'))
    has_transformations = len(cycle.get('transformations', [])) > 0
    should_run = all([node_type == NodeType.CYCLE.value, has_transformations])
    logShouldRun(cycle, MODEL_LOG, None, should_run)
    return should_run


def run(cycle: dict):
    should_run = _should_run(cycle)
    transformations = list(filter(_should_run_transformation, cycle.get('transformations', []))) if should_run else []
    return reduce(_run_transformation(cycle), transformations, [])
