from hestia_earth.schema import MeasurementStatsDefinition, MeasurementMethodClassification

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from .utils import download, find_existing_measurement, has_geospatial_data, should_download
from . import MODEL

REQUIREMENTS = {
    "Site": {
        "or": [
            {"latitude": "", "longitude": ""},
            {"boundary": {}},
            {"region": {"@type": "Term", "termType": "region"}}
        ]
    }
}
RETURNS = {
    "Measurement": [{
        "value": "",
        "statsDefinition": "spatial",
        "methodClassification": "geospatial dataset"
    }]
}
TERM_ID = 'heavyWinterPrecipitation'
EE_PARAMS = {
    'collection': 'correction_winter-type_precipitation',
    'ee_type': 'raster',
    'reducer': 'mode',
    'fields': 'mode'
}
BIBLIO_TITLE = 'Modelling spatially explicit impacts from phosphorus emissions in agriculture'


def _measurement(value: float):
    measurement = _new_measurement(TERM_ID, None, BIBLIO_TITLE)
    measurement['value'] = [value]
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    measurement['methodClassification'] = MeasurementMethodClassification.GEOSPATIAL_DATASET.value
    return measurement


def _download(site: dict):
    value = download(TERM_ID, site, EE_PARAMS).get(EE_PARAMS['reducer'])
    return 1 if value == 1 else (0 if value == 0.1 else None)


def _run(site: dict):
    value = find_existing_measurement(TERM_ID, site) or _download(site)
    return [] if value is None else [_measurement(value)]


def _should_run(site: dict):
    contains_geospatial_data = has_geospatial_data(site)
    below_max_area_size = should_download(TERM_ID, site)

    logRequirements(site, model=MODEL, term=TERM_ID,
                    contains_geospatial_data=contains_geospatial_data,
                    below_max_area_size=below_max_area_size)

    should_run = all([contains_geospatial_data, below_max_area_size])
    logShouldRun(site, MODEL, TERM_ID, should_run)
    return should_run


def run(site: dict): return _run(site) if _should_run(site) else []
