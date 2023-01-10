import pytest
from code import division


def test_division_good():
    assert division(10, 5) == 2


@pytest.mark.parametrize('expected_exception, divider', [(ZeroDivisionError, 0), (TypeError, 'str')])
def test_fail_exceptions(expected_exception, divider):
    with pytest.raises(expected_exception):
        division(10, divider)
