from hestia_earth.schema import MeasurementStatsDefinition, MeasurementMethodClassification

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.measurement import _new_measurement
from .utils import download, find_existing_measurement, has_geospatial_data, should_download
from . import MODEL
from .temperatureAnnual import _to_celcius

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
        "startDate": "",
        "endDate": "",
        "statsDefinition": "spatial",
        "methodClassification": "geospatial dataset"
    }]
}
TERM_ID = 'temperatureLongTermAnnualMean'
START_DATE = '1979-01-01'
END_DATE = '2020-12-31'
EE_PARAMS = {
    'collection': 'ECMWF/ERA5/MONTHLY',
    'ee_type': 'raster_by_period',
    'reducer': 'mean',
    'band_name': 'mean_2m_air_temperature',
    'start_date': START_DATE,
    'end_date': END_DATE
}
BIBLIO_TITLE = 'ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate'


def _measurement(value: float):
    measurement = _new_measurement(TERM_ID, None, BIBLIO_TITLE)
    measurement['value'] = [value]
    measurement['statsDefinition'] = MeasurementStatsDefinition.SPATIAL.value
    measurement['methodClassification'] = MeasurementMethodClassification.GEOSPATIAL_DATASET.value
    measurement['startDate'] = START_DATE
    measurement['endDate'] = END_DATE
    return measurement


def _download(site: dict):
    return _to_celcius(download(TERM_ID, site, EE_PARAMS).get(EE_PARAMS['reducer']))


def _run(site: dict):
    value = find_existing_measurement(TERM_ID, site) or _download(site)
    return [_measurement(value)] if value is not None else []


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
