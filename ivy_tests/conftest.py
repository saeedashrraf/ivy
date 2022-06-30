from hypothesis import settings, HealthCheck
from pytest import mark
settings.register_profile("ci", suppress_health_check=(HealthCheck(3),))
settings.load_profile("ci")

skip_ids = ['ivy_tests/test_array_api/array_api_tests/test_special_cases.py::test_iop[__iadd__(x1_i is NaN or x2_i is NaN) -> NaN]']


def pytest_collection_modifyitems(config, items):
    for item in items:
        # skip if specified in skips.txt
        for id_ in skip_ids:
            if item.nodeid.startswith(id_):
                item.add_marker(mark.skip(reason="Skipping reason"))
                break
