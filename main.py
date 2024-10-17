from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt


if __name__ == '__main__':
    print(dt.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
    flag = input("Если хотите посчитать зарплату сотрудника нажмите 1, Узнать информацию о сотруднике 2: ")
    if flag == '1':
        print(calculate_salary())
    elif flag == '2':
        print(get_employees())
    else:
        print('Неверная команда')
