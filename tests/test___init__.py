import pytest
from xprmind import fx


@pytest.fixture
def my_car():
    return 50


speed_data = {45, 50, 55, 100}


@pytest.mark.parametrize("speed_brake", speed_data)
def test_fx(my_car, speed_brake):
    assert fx() is None


@pytest.mark.parametrize("speed_brake", speed_data)
def test_fx2(my_car, speed_brake):
    assert fx() is None
