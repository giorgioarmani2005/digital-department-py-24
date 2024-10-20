money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money=money_capital
num_month=0
while money+salary>spend:
    money+=salary
    money-=spend
    spend+=spend*increase
    num_month+=1

print("Количество месяцев, которое можно протянуть без долгов:", num_month)
