import threading
import random
import fightclass




class BotFight(fightclass.Fight):

    def take_pokemon(self):
        super(BotFight, self).take_pokemon()

    def use_pokemon(self, poke, enemy):
            move = str(random.randint(1,3))
            if move == '1':
                poke.attack(poke, enemy, 1)
            elif move == '2':
                poke.Special1(poke, enemy, 1)
            elif move == '3':
                poke.Special2(poke, enemy, 1)

    def Battle(self):
        super(BotFight, self).Battle()


