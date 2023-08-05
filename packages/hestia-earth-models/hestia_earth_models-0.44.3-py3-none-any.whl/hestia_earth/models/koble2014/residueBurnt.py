from hestia_earth.utils.lookup import get_table_value, download_lookup, column_name
from hestia_earth.utils.tools import safe_parse_float

from hestia_earth.models.log import logRequirements, debugMissingLookup
from hestia_earth.models.utils.term import get_lookup_value
from . import MODEL
from .utils import _should_run, _practice

REQUIREMENTS = {
    "Cycle": {
        "completeness.cropResidue": "False",
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"}
        }
    }
}
LOOKUPS = {
    "crop": ["cropGroupingResidue", "Combustion_Factor_crop_residue"],
    "region-crop-cropGroupingResidue-burnt": "using result from `cropGroupingResidue`"
}
RETURNS = {
    "Practice": [{
        "value": "",
        "statsDefinition": "modelled"
    }]
}
TERM_ID = 'residueBurnt'
LOOKUP_NAME = 'region-crop-cropGroupingResidue-burnt.csv'


def _get_default_percent(cycle: dict, term: dict, country_id: str):
    crop_grouping = get_lookup_value(term, LOOKUPS['crop'][0], model=MODEL, term=TERM_ID)
    lookup = download_lookup(LOOKUP_NAME)
    percent = safe_parse_float(
        get_table_value(lookup, 'termid', country_id, column_name(crop_grouping)), None
    ) if crop_grouping else None
    debugMissingLookup(LOOKUP_NAME, 'termid', country_id, crop_grouping, percent, model=MODEL)
    comb_factor = safe_parse_float(get_lookup_value(term, LOOKUPS['crop'][1], model=MODEL, term=TERM_ID))
    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    crop_grouping=crop_grouping,
                    country_id=country_id,
                    percent=percent,
                    comb_factor=comb_factor)
    return percent if comb_factor is None or percent is None else percent * comb_factor


def _run(cycle: dict, remaining_value: float, primary_product: dict, country_id: str):
    term = primary_product.get('term', {})
    value = _get_default_percent(cycle, term, country_id)
    return [] if value is None else [_practice(TERM_ID, min(round(value * 100, 2), remaining_value))]


def run(cycle: dict):
    should_run, remaining_value, primary_product, country_id = _should_run(TERM_ID, cycle, require_country=True)
    return _run(cycle, remaining_value, primary_product, country_id) if should_run else []
