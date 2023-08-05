from hestia_earth.schema import TermTermType, CycleFunctionalUnit, PracticeStatsDefinition
from hestia_earth.utils.model import filter_list_term_type

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.practice import _new_practice
from hestia_earth.models.utils.input import get_total_irrigation_m3
from hestia_earth.models.utils.completeness import _is_term_type_complete
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "completeness.water": "",
        "functionalUnit": "1 ha",
        "none": {
            "practices": [{"@type": "Practice", "units": "%", "term.termType": "waterRegime"}]
        },
        "optional": {
            "inputs": [{"@type": "Input", "term.termType": "water", "value": ""}]
        }
    }
}
RETURNS = {
    "Practice": [{
        "value": "",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'irrigated'
MIN_IRRIGATION_M3 = 250


def _practice(value: float):
    practice = _new_practice(TERM_ID)
    practice['value'] = [value]
    practice['statsDefinition'] = PracticeStatsDefinition.MODELLED.value
    return practice


def _run(irrigation_m3: float):
    value = 100 if irrigation_m3 > MIN_IRRIGATION_M3 else 0
    return [_practice(value)]


def _should_run(cycle: dict):
    functional_unit = cycle.get('functionalUnit')
    water_complete = _is_term_type_complete(cycle, {'termType': TermTermType.WATER.value})
    irrigation_value_m3 = get_total_irrigation_m3(cycle)

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    water_complete=water_complete,
                    irrigation_value_m3=irrigation_value_m3)

    should_run = all([
        functional_unit == CycleFunctionalUnit._1_HA.value,
        any([water_complete, irrigation_value_m3 > MIN_IRRIGATION_M3])
    ])
    logShouldRun(cycle, MODEL, TERM_ID, should_run)
    return should_run, irrigation_value_m3


def run(cycle: dict):
    water_regime = filter_list_term_type(cycle.get('practices', []), TermTermType.WATERREGIME)
    # skip model if user already specified the percent of irrigation
    has_irrigation_practice = any([p.get('term', {}).get('units', '') == '%' for p in water_regime])
    should_run, irrigation_m3 = _should_run(cycle) if not has_irrigation_practice else (False, 0)
    return _run(irrigation_m3) if should_run else []
