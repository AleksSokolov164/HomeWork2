"""
(МОДУЛЬ 1)
объект для описания: стол
 Объявить переменные основных типов данных для описания этого объекта:
назначение (тип строка),  количество ножек(тип целое число),  наличие ящиков (логический тип), количество ящиков (тип целое число),
цена (число с плавающей точкой)
В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных
"""

table = 'Стол детский'
leg = 4
box = True
nbox = 2
price = 10.23
print('Название стола',table,type(table),sep=" ")
print('количество ножек',leg,type(leg),sep=" ")
print('наличие ящиков ',box,type(box),sep=" ")
print('количество ящиков',nbox,type(nbox),sep=" ")
print('цена',price,type(price),sep=" ")
