# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# игра для двух человек:

from random import randint


def conditions(name):
    x = int(input(f'{name}, возьмите конфеты, от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, можно взять любое количество конфет от 1 до 28: '))
    return x


def count(quantity):
    print(f'Теперь на столе {quantity} конфет')


player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')
quantity = 2021
print('Бросаем монетку. У кого орел, тот ходит первым')
flag = randint(0, 1)
if flag:
    print('Первый ход твой, ', player1)
else:
    print('Первый ход твой, ', player2)

counter1 = 0
counter2 = 0

while quantity > 28:
    if flag:
        k = conditions(player1)
        counter1 += k
        quantity -= k
        flag = False
        count(quantity)
    else:
        k = conditions(player2)
        counter2 += k
        quantity -= k
        flag = True
        count(quantity)

if flag:
    print(f'Выиграл {player1}')
else:
    print(f'Выиграл {player2}')
