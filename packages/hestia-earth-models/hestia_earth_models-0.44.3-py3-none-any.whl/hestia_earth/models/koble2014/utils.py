from functools import reduce
from hestia_earth.schema import TermTermType, PracticeStatsDefinition
from hestia_earth.utils.model import find_primary_product, find_term_match
from hestia_earth.utils.tools import list_sum

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.completeness import _is_term_type_incomplete
from hestia_earth.models.utils.practice import _new_practice
from hestia_earth.models.utils.term import get_crop_residue_management_terms
from . import MODEL


def _practice(term_id: str, value: float):
    practice = _new_practice(term_id, MODEL)
    practice['value'] = [value]
    practice['statsDefinition'] = PracticeStatsDefinition.MODELLED.value
    return practice


def _model_value(term_id: str, practices: list):
    return list_sum(find_term_match(practices, term_id).get('value', [0]))


def _should_run(term_id: str, cycle: dict, require_country: bool = False):
    primary_product = find_primary_product(cycle)
    has_primary_product = primary_product is not None
    crop_residue_incomplete = _is_term_type_incomplete(cycle, {'termType': TermTermType.CROPRESIDUE.value})
    practices = cycle.get('practices', [])
    residue_terms = get_crop_residue_management_terms()
    remaining_value = reduce(lambda prev, term: prev - _model_value(term, practices), residue_terms, 100)
    has_remaining_value = remaining_value > 0

    country_id = cycle.get('site', {}).get('country', {}).get('@id')

    logRequirements(cycle, model=MODEL, term=term_id,
                    has_primary_product=has_primary_product,
                    crop_residue_incomplete=crop_residue_incomplete,
                    has_remaining_value=has_remaining_value,
                    country_id=country_id)

    should_run = all([
        has_primary_product, crop_residue_incomplete, has_remaining_value,
        not require_country or country_id
    ])
    logShouldRun(cycle, MODEL, term_id, should_run)
    return should_run, remaining_value, primary_product, country_id
