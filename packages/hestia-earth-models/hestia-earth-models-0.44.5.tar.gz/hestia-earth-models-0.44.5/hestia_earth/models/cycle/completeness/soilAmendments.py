"""
Completeness Soil Amendments

This model checks if we have the requirements below and updates the
[Data Completeness](https://hestia.earth/schema/Completeness#soilAmendments) value.
"""
from hestia_earth.models.log import logRequirements
from hestia_earth.models.utils import is_from_model
from hestia_earth.models.utils.measurement import most_relevant_measurement, measurement_value
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "completeness.soilAmendments": "False",
        "endDate": "",
        "site": {
            "@type": "Site",
            "measurements": [{"@type": "Measurement", "value": "", "term.@id": "soilPh"}]
        }
    }
}
RETURNS = {
    "Completeness": {
        "soilAmendments": ""
    }
}
MODEL_KEY = 'soilAmendments'


def run(cycle: dict):
    end_date = cycle.get('endDate')
    measurements = cycle.get('site', {}).get('measurements', [])
    soilPh_measurement = most_relevant_measurement(measurements, 'soilPh', end_date)
    soilPh = measurement_value(soilPh_measurement)

    soilPh_added = is_from_model(soilPh_measurement)
    soilPh_above_6_5 = soilPh > 6.5

    logRequirements(cycle, model=MODEL, term=None, key=MODEL_KEY,
                    soilPh_added=soilPh_added,
                    soilPh_above_6_5=soilPh_above_6_5)

    return all([soilPh_added, soilPh_above_6_5])
