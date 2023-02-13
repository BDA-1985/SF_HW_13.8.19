numbers_tickets = int(input('Введите количество покупаемых билетов: '))

numbers_ages = []

"""Присваиваем возраст каждому участнику конференции"""
for i in range(0, numbers_tickets):
    input_value = int(input(f'Введите возраст участника конференции №{i + 1}: '))
    numbers_ages.append(input_value)

"""В зависимости от возраста выбираем цену билетов"""
def prise(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    else:
        return 1390

"""Расчитываем общую стоимость билетов"""
full_prise = sum(map(prise, numbers_ages))

"""Устанавливаем скидку при покупке более трёх билетов"""

discount_prise = int(full_prise * 0.9)
if numbers_tickets > 3:
    print(f'Стоимость билетов со скидкой: '+str(discount_prise)+' руб.')
else:
    print(f'Стоимость билетов: '+str(full_prise)+' руб.')
