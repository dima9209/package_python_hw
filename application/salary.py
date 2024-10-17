def calculate_salary():
    count_days = int(input("Укажите количество отработанных дней:"))
    rate = 12000
    return f'{count_days * rate} руб.'