from unittest.mock import patch

from tests.utils import TERM
from hestia_earth.models.utils.emission import _new_emission

class_path = 'hestia_earth.models.utils.emission'


@patch(f'{class_path}._include_methodModel', side_effect=lambda n, x: n)
@patch(f'{class_path}.download_hestia', return_value=TERM)
def test_new_emission(*args):
    # with a Term as string
    emission = _new_emission('term')
    assert emission == {
        '@type': 'Emission',
        'term': TERM
    }

    # with a Term as dict
    emission = _new_emission(TERM)
    assert emission == {
        '@type': 'Emission',
        'term': TERM
    }
