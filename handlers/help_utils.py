def get_salary(salary: int, month: str):
    data = {
        'Декабрь': {'days_to_avans': 10, 'work_day': 20},
        'Январь': {'days_to_avans': 5, 'work_day': 17},
        'Февраль': {'days_to_avans': 11, 'work_day': 20},
        'Март': {'days_to_avans': 10, 'work_day': 20},
        'Апрель': {'days_to_avans': 11, 'work_day': 21},
        'Май': {'days_to_avans': 8, 'work_day': 20},
        'Июнь': {'days_to_avans': 9, 'work_day': 19},
        'Июль': {'days_to_avans': 11, 'work_day': 23},
        'Август': {'days_to_avans': 11, 'work_day': 22},
        'Сентябрь': {'days_to_avans': 10, 'work_day': 21},
        'Октябрь': {'days_to_avans': 11, 'work_day': 23},
        'Ноябрь': {'days_to_avans': 10, 'work_day': 21},
    }

    month = data.get(month)
    wd = month.get('work_day')
    dta = month.get('days_to_avans')

    avans = round((int(salary) / wd) * dta)
    zepeshka = round(int(salary) - avans)
    return {
        'avans': avans,
        'zepeshka': zepeshka,
    }
