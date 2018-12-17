import pytest

import app.calculate_credit


@pytest.mark.parametrize('credit_sum, percent_in_year, credit_months, expected', [
    (40_000, 22, 24, 2075.1),
    (0, 10, 12, 0.0),
    pytest.param(100_000, 0, 0, 0, marks=pytest.mark.xfail)
])
def test_calculate_annuitet_credit(credit_sum, percent_in_year, credit_months, expected):
    actual = app.calculate_credit.calculate_annuitet_credit(credit_sum, percent_in_year, credit_months)

    assert expected == pytest.approx(actual, 0.1)


@pytest.mark.parametrize('credit_sum, percent_in_year, credit_months, expected', [
    (120_000, 10, 12,
     110000.0)
])
def calculate_differentiated_credit(credit_sum, percent_in_year, credit_months, expected):
    actual = app.calculate_credit.calculate_differentiated_credit(credit_sum, percent_in_year, credit_months)

    assert expected == pytest.approx(actual, 0.1)
