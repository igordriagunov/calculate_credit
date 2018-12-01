import app.calculate_credit


def test_calculate_annuitet_credit(credit_sum, percent_in_year, credit_months, expected):
    actual = app.calculate_credit.calculate_annuitet_credit(credit_sum, percent_in_year, credit_months)

    assert expected == actual
