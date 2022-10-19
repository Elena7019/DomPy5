# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# b) Подумайте как наделить бота ""интеллектом""

# b) игра умный компьютер против человека:

from random import randint


def conditions(name):
    global x
    if name == player1:
        x = int(input(f'{name}, возьмите конфеты, от 1 до 28: '))
        print('Игрок по имени ', name, 'взял', x, 'конфет')
    elif name == player2:
        if quantity % 29 != 0:
            x = quantity - (quantity // 29) * 29
        else:
            x = 1
        print('Компьютер Умный Вася взял ', x, ' конфет')
    while x < 1 or x > 28:
        x = int(input(f'{name}, можно взять любое количество конфет от 1 до 28: '))
    return x


def count(quantity):
    print(f'Теперь на столе {quantity} конфет')


global x
quantity = 2021
player1 = input('Имя первого игрока: ')
player2 = 'компьютер Умный Вася'
print(player1, ', с тобой играет компьютер Умный Вася')

print('Бросаем монетку. У кого орел, тот ходит первым')
flag = randint(0, 1)
if flag == 1:
    print('Первый ход достался игроку по имени ', player1)
else:
    print('Первый ход достался игроку по имени ', player2)

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
    print(f'Выиграл игрок по имени {player1}')
else:
    print(f'Выиграл игрок по имени {player2}')
