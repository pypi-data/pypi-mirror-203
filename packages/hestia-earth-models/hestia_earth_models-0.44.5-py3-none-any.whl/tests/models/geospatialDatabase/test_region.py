from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_download_term

from hestia_earth.models.geospatialDatabase.region import MODEL, MODEL_KEY, run, _should_run

class_path = f"hestia_earth.models.{MODEL}.{MODEL_KEY}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{MODEL_KEY}"


@patch(f"{class_path}.should_download", return_value=True)
@patch(f"{class_path}.has_geospatial_data")
def test_should_run(mock_has_geospatial_data, *args):
    mock_has_geospatial_data.return_value = True
    assert _should_run({}) is True

    mock_has_geospatial_data.return_value = False
    assert not _should_run({})


@patch(f"{class_path}.download_hestia", side_effect=fake_download_term)
@patch(f"{class_path}.download", return_value={})
def test_run(mock_download, *args):
    with open(f"{fixtures_path}/{MODEL}/site.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    run(site)
    assert mock_download.call_count == 5
