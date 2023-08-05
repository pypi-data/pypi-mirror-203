from unittest.mock import patch
import json
from tests.utils import fixtures_path

from hestia_earth.models.cycle.input.properties import MODEL_KEY, run

class_path = f"hestia_earth.models.cycle.input.{MODEL_KEY}"
fixtures_folder = f"{fixtures_path}/cycle/input/{MODEL_KEY}"


with open(f"{fixtures_folder}/cycle-properties.jsonld", encoding='utf-8') as f:
    connected_cycle = json.load(f)
with open(f"{fixtures_folder}/impactAssessment.jsonld", encoding='utf-8') as f:
    connected_impact = json.load(f)


def fake_load_calculated_node(node, node_type):
    return connected_cycle if node_type.value == 'Cycle' else connected_impact


@patch(f"{class_path}._load_calculated_node", side_effect=fake_load_calculated_node)
def test_run(*args):
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    result = run(cycle)
    assert result == expected
