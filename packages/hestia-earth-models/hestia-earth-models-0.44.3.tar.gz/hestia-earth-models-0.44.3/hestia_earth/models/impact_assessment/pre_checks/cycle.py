"""
Impact Assessment Pre Checks Cycle

Some ImpactAssessment models need a full version of the linked [Cycle](https://hestia.earth/schema/Cycle) to run.
This model will fetch the complete version of the [Cycle](https://hestia.earth/schema/Cycle) and include it.
"""
from hestia_earth.schema import SchemaType

from hestia_earth.models.utils import _load_calculated_node

REQUIREMENTS = {
    "ImpactAssessment": {
        "cycle": {
            "@type": "Cycle",
            "@id": ""
        }
    }
}
RETURNS = {
    "ImpactAssessment": {
        "cycle": {"@type": "Cycle"}
    }
}
MODEL_KEY = 'cycle'


def _run(impact: dict):
    cycle = _load_calculated_node(impact.get(MODEL_KEY, {}), SchemaType.CYCLE)
    site = _load_calculated_node(cycle.get('site', {}), SchemaType.SITE)
    if site:
        cycle['site'] = site
    return cycle


def _should_run(impact: dict):
    cycle_id = impact.get(MODEL_KEY, {}).get('@id')
    run = cycle_id is not None
    return run


def run(impact: dict): return {**impact, **({MODEL_KEY: _run(impact)} if _should_run(impact) else {})}
