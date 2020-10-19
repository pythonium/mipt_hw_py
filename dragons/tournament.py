# coding: utf-8
# license: GPLv3

from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = list(map(int, input(message).split()))
        except ValueError:
            print('Вы ввели недопустимые символы')

    return answer

def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        if dragon._color is None:
            print('Вышел тролль!')
        else:
            print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                hero._xp += 10
                print('Верно! \n** дракон кричит от боли **') if dragon._color is not None else print('Верно! \n** тролль кричит от боли **')
            else:
                dragon.attack(hero)
                hero._xp -= 10
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Тролль повержен!\n') if dragon._color is None else print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._xp)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 4
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 4)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
