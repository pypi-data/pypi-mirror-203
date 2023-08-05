from hestia_earth.schema import PracticeStatsDefinition
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.tools import safe_parse_float

from hestia_earth.models.log import logRequirements, debugMissingLookup, logShouldRun
from hestia_earth.models.utils.practice import _new_practice
from hestia_earth.models.utils.product import has_flooded_rice
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "cycleDuration": "",
        "products": [{
            "@type": "Product",
            "primary": "True",
            "value": "",
            "term.@id": ["riceGrainInHuskFlooded", "ricePlantFlooded"],
            "term.termType": "crop"
        }],
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"}
        }
    }
}
LOOKUPS = {
    "region-ch4ef-IPCC2019": [
        "Rice_croppingDuration_days", "Rice_croppingDuration_days_min", "Rice_croppingDuration_days_max",
        "Rice_croppingDuration_days_sd"
    ]
}
RETURNS = {
    "Practice": [{
        "value": "",
        "min": "",
        "max": "",
        "sd": "",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'croppingDuration'
LOOKUP_TABLE = 'region-ch4ef-IPCC2019.csv'
LOOKUP_COL_PREFIX = 'Rice_croppingDuration_days'


def _practice(value: float, min: float, max: float, sd: float):
    practice = _new_practice(TERM_ID, MODEL)
    practice['value'] = [value]
    practice['min'] = [min]
    practice['max'] = [max]
    practice['sd'] = [sd]
    practice['statsDefinition'] = PracticeStatsDefinition.MODELLED.value
    return practice


def _get_value(country: str, col: str):
    lookup = download_lookup(LOOKUP_TABLE)
    value = safe_parse_float(get_table_value(lookup, 'termid', country, column_name(col)))
    debugMissingLookup(LOOKUP_TABLE, 'termid', country, col, value, model=MODEL, term=TERM_ID)
    return value


def _run(country: str, cycleDuration: float):
    value = _get_value(country, LOOKUP_COL_PREFIX)
    min = _get_value(country, f"{LOOKUP_COL_PREFIX}_min")
    max = _get_value(country, f"{LOOKUP_COL_PREFIX}_max")
    sd = _get_value(country, f"{LOOKUP_COL_PREFIX}_sd")
    return [_practice(value, min, max, sd)] if value <= cycleDuration else []


def _should_run(cycle: dict):
    country = cycle.get('site', {}).get('country', {}).get('@id')
    cycleDuration = cycle.get('cycleDuration', 0)
    flooded_rice = has_flooded_rice(cycle.get('products', []))

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    country=country,
                    cycleDuration=cycleDuration,
                    flooded_rice=flooded_rice)

    should_run = all([country, cycleDuration, flooded_rice])
    logShouldRun(cycle, MODEL, TERM_ID, should_run)
    return should_run, country, cycleDuration


def run(cycle: dict):
    should_run, country, cycleDuration = _should_run(cycle)
    return _run(country, cycleDuration) if should_run else []
