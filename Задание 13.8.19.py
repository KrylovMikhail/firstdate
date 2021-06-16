tickets = int(input('Какое колличество билетов желаете приобрести?\n',))
if tickets <= 0:
    print('Если идти не хотите, то трогать тут ничего не надо!')

price = 0

for participant in range(tickets):
    age = int(input('Уточните возраст участника:\n'))
    if 0 < age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    elif age >= 25:
        price += 1390
    else:
        print('Мы пока не готовы принять не родившихся людей, что-то пошло не так')
        break

if tickets <= 3:
    print('Цена:\n', price)
else:
    price = price*0.9
    print('Цена с учетом скидки в 10% за группу больше 3 человек:\n', price)

