def calculate_annuitet_credit(credit_sum, percent_in_year, credit_months):
    """
    >>> calculate_annuitet_credit(40_000, 22, 24) # doctest: +ELLIPSIS
    2075.12...
    # >>> calculate_annuitet_credit(100_000, 0, 0)
    # 0
    >>> calculate_annuitet_credit(1_000_000, 24, 36) # doctest: +ELLIPSIS
    39232.85...
    >>> calculate_annuitet_credit(0 , 10, 12)
    0.0
    """
    twelve_months = 12
    hundred_percent = 100
    month_percent = (percent_in_year / hundred_percent) / twelve_months
    monthly_payment = credit_sum * (month_percent / (1 - (1 + month_percent) ** (-credit_months)))
    final_sum = monthly_payment * credit_months
    overpayment = final_sum - credit_sum
    # print("Переплата: ", overpayment)
    # print("Общая сумма кредита : ", final_sum)
    # print("Ежемесячный платеж : ", monthly_payment)
    return monthly_payment


print(calculate_annuitet_credit(40_000, 22, 24))


def calculate_differentiated_credit(credit_sum, percent_in_year, credit_months):
    """
    >>> calculate_differentiated_credit(120_000, 10, 12) # doctest: +ELLIPSIS
    110000.0
    1000.0
    100000.0
    916.66...
    90000.0
    833.33...
    80000.0
    750.0
    70000.0
    666.66...
    60000.0
    583.33...
    50000.0
    500.0
    40000.0
    416.66...
    30000.0
    333.33...
    20000.0
    250.0
    10000.0
    166.66...
    0.0
    83.33...
    0.0
    """

    main_payment = credit_sum / credit_months
    print(main_payment)
    while credit_sum > 0:
        damping_payment = (credit_sum * percent_in_year) / (100 * 12)
        credit_sum = credit_sum - main_payment
        # print(credit_sum)
        print(damping_payment)
    return credit_sum


print(calculate_differentiated_credit(120_000, 10, 12))
print("-----------------")
print(calculate_differentiated_credit(635_000, 21, 24))
