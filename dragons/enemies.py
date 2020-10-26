# coding: utf-8
# license: GPLv3

from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    random_enemy_type = choice(enemy_types)
    enemy = random_enemy_type()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

#    def cheat(self, answer):
 #       return answer == dragon._cheat


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer([x + y])
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer([x * y])
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer([x - y])
        return self.__quest

class Troll(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = None

    def question(self):
        n = randint(1,100)
        self.__quest = "Разложи на простые множители " + str(n) + "\n Записывай в порядке возрастания"

        Ans = []

        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        ans_str = " ".join(map(str, Ans))


        self.set_answer(Ans)
        return self.__quest

enemy_types = [GreenDragon, RedDragon, BlackDragon, Troll]
