bilet = int(input('Сколько билетов хотите купить: '))
list_ages = []
for i in range(0, bilet):
    input_age = int(input(f'Введите возраст участника №{i + 1}:\n'))
    list_ages.append(input_age)
    def prise(age):
         if age < 18:
             return 0
         elif 18 <= age < 25:
             return 0
         else:
             return 1390
    full_prise = sum(map(prise, list_ages))
discount_prise = int(full_prise * 0.9)
if bilet > 3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', full_prise, "руб.")