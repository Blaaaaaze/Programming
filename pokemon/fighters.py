class Pokemon:
    #конструктор
    def __init__(self):
        #Инкапсуляция: все переменные запривачены. Доступ к ним не из класса Pokemon доступен с помощью гетеров и сетеров
        self.__hit = 20 #базовая атака
        self.__hp = 100 #базовое здоровье
        self.__name = "Pokemon" #имя обычно совпадает с классом покемона
        self.__status = "Normal" #Статусы: Normal - нет эффектов, Stan - оглушен, Fire - горит (не действует на покемона воды) - -2 хп за ход любого покемона, Poison  - -2 хп за ход любого покемона, Shield(возможно с доп хп) - имеет защиту(невосприимчивость к эффектам)
        self.__possible_move = 1 #Если один - покемон может ходить, если ноль, то покемон пропускает ход, т.е. находится в стане
        self.__time_effect = 0 #счетчик действия эффектов: Щит - 2 хода, Оглушение - 1 ход, горение - 2 хода, отравление - 2 хода
        self.__type = 'Normal' #тип покемона указывается в классе каждого покемона

    #геты и сеты, доступ ко всем атрибутам класса
    #Все геты
    def get_hit(self):
        return self.__hit

    def get_hp(self):
        return self.__hp

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def get_PossMove(self):
        return self.__possible_move

    def get_timeEff(self):
        return self.__time_effect

    def get_type(self):
        return self.__type

    #Все сеты
    def set_hp(self, hp):
        self.__hp = hp

    def set_hit(self, hit):
        self.__hit = hit

    def set_name(self, name):
        self.__name = name

    def set_status(self, status):
        self.__status = status

    def set_PossMove(self, possible_move):
        self.__possible_move = possible_move

    def set_timeEff(self, time_effect):
        self.__time_effect = time_effect

    def set_type(self, type):
        self.__type = type

    #базовая атака
    def attack(self, me, enemy):
        enemy.set_hp(enemy.get_hp() - me.get_hit())
        print(f"Покемон {me.get_name()} совершил базовую атаку мощностью {me.get_hit()}. Покемон {enemy.get_name()} теперь имеет {enemy.get_hp()} очков здоровья. ")

    #базовые спешл атаки
    #Здесь будет перегрузка в дочерних классах
    def Special1(self, enemy):
        if enemy.get_status() != "Shield":
            enemy.set_hp(enemy.get_hp() -(self.__hit)*2)
            print(f'Покемон {self.__name} проводит двйоную атаку\n'
                  f'Покемон {enemy.get_name()} теряет {(self.__hit)*2}. Теперь его здоровье равно {enemy.get_hp()}')

    #Здесь тоже будет перегрузка
    def Special2(self):
        self.__hp = self.__hp + 30
        print(f'Покемон {self.__name} восстановил 30 очков здоровья. Теперь его здоровье равно {self.__hp}')



    #Проверка состояния покемона
    #Важно! Реализовано так, что применение щита, снимает любой негативный эффект. Также возможно наличии лишь одного эффекта в один период времени. Мб в будущем будет исправлено
    def check_my_status(self):
        if self.__status == "Normal":
            self.__possible_move = 1
        if self.__status == "Shield":
            print(f"Покемон {self.__name} имеет щит. Он защищен от негативных эффектов")
            print(f'осталось ходов до окончания щита: {self.__time_effect}')
        if self.__status == "Stan":
            self.__possible_move = 0
            print(f"Покемон {self.__name} оглушен. Пропуск хода")
            print(f'осталось ходов до восстановления: {self.__time_effect}')
        if self.__status == "Fire" and self.__type != "Water":
            self.__hp -= 3
            print(f'Покемон {self.__name} горит. У него отнялось 3 hp. Теперь {self.__name} имеет {self.__hp} очков здоровья.')
            print(f'осталось ходов до восстановления: {self.__time_effect}')
        if self.__status == "Poison":
            self.__hp -= 2
            print(f'Покемон {self.__name} отравлен. У него отнялось 2 hp. Теперь {self.__name} имеет {self.__hp} очков здоровья.')
            print(f'осталось ходов до восстановления: {self.__time_effect}')
        self.__time_effect -= 1 #Счетчик, чтобы все эффекты скидывались
        if self.__time_effect == 0: #Когда счетчик закончится, состояние будет возвращено на Normal
            self.__status = 'Normal'






#Классы покемонов(пока 4 стартовых, потом мб добавлю еще)
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__()
        self.__type = "Electric" #тип либо ни на что не повлияет либо я введу контртипы

    #Типы не могут изменяться, поэтому только гет
    def get_type(self):
        return self.__type


    #эффекты спешл атак взяты с форума покемонов (комментарий около функции - название способности со странички покемона) url: https://pokemondb.net/
    #Абилки не соответствуют полностью с описанием на сайте, так как все делается в учебных целях и есть интерес сделать разные механики
    #Все спешл атаки, у которых используется атрибут enemy являются атакующими, т.е. изменяют состояние другого покемона
    #Реализована перегрузка(мб не оч корректно)
    def Special1(self,me, enemy): #Nuzzle
        if enemy.get_status() != 'Shield':
            enemy.set_status('Stan')
            enemy.set_timeEff(1)
            enemy.set_hp(enemy.get_hp() - 5)
            print(f"У покемона {enemy.get_name()} не было щита, поэтому теперь он углушен")

    # Реализована перегрузка(мб не оч корректно)
    def Special2(self,me, enemy): #Iron_tail
        if enemy.get_status() == "Shield":
            enemy.set_hp(enemy.get_hp() - 10)
            enemy.set_status("Normal")
            print(f"У покемона {enemy.get_name()} был щит. Теперь он сбит\n"
                  f"Покемон {enemy.get_name()} потерял 10 очков здоровья. Теперь его здоровье равно {enemy.get_hp()}")
        else:
            enemy.set_hp(enemy.get_hp() - 30)
            print(f"У покемона {enemy.get_name()} не было щита\n"
                  f"Покемон {enemy.get_name()} потерял 30 очков здоровья. Теперь его здоровье равно {enemy.get_hp()}")


    def tutorial(self, me): #Стартовая инфа о выбранном классе покемона
        print(f"Вы выбрали покемона {me.get_name()}\n"
              f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Nuzzle - Станит покемона-оппонента\n"
              f"3) Iron_tail - Если у противника есть щит, то он сбивается и наносится 30% от урона способности, если щита нет - наносится 30 едиинц урона\n")

    def fight_help(self, me): #напоминалка в бою
        print(f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Nuzzle - Станит покемона-оппонента\n"
              f"3) Iron_tail - Если у противника есть щит, то он сбивается и наносится 30% от урона способности, если щита нет - наносится 30 едиинц урона\n")

#Далее по аналогии с пикачу, поэтому комментариев не будет (ток если не появится что-то уникальное)

class Charmander(Pokemon):
    def __init__(self):
        super().__init__()
        self.__type = "Fire"

    def get_type(self):
        return self.__type

    #Спешл атаки:
    # Реализована перегрузка(мб не оч корректно)
    def Special1(self, me, enemy): #FireFang
        if enemy.get_status() != "Shield" and enemy.get_type() != 'Water':
            enemy.set_status("Fire")
            enemy.set_timeEff(2)
            enemy.set_hp(enemy.get_hp() - 10)
            print(f"Покемон {enemy.get_name()} атакован. Он потерял 10 очков здоровья. Теперь его здоровье равно {enemy.get_hp()}\n"
                  f"Покемон {enemy.get_name()} горит\n"
                  f"Покемон {enemy.get_name()} потерял 3 очка здоровья. Теперь его здоровье равно {enemy.get_hp()}\n"
                  f"Осталось ходов до окончания эффекта: {me.get_timeEff()}")
        else:
            if enemy.get_status() == "Shield":
                print(f'Покемон {enemy.get_name()} имеет щит. Способность не сработала')
            elif enemy.get_type() == 'Water':
                print(f'Покемон {enemy.get_name()} является водным типом. Способность не сработала')


    #Защитная способность, поэтому действует на себя, а не на противника(enemy не задействован)
    # Реализована перегрузка(мб не оч корректно)
    def Special2(self, me, enemy): #Protect
        me.set_status("Shield")
        me.set_hp(me.get_hp() + 10)
        me.set_timeEff(2)
        print(f"Покемон {me.get_name()} получил щит. Теперь он неуязвим с эффектами контроля\n"
              f"Покемон {me.get_name()} получает 10 дополнительных очков здоровья от щита. Теперь его здоровье равно {me.get_hp()}\n"
              f"До конца эффекта щита осталось {me.get_timeEff()} ходов")


    def tutorial(self, me):  # Стартовая инфа о выбранном классе покемона
        print(f"Вы выбрали покемона {me.get_name()}\n"
              f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Fire Fang - Поджигает покемона противника\n"
              f"3) Protect - Устанавливает Щит на покемона\n")

    def fight_help(self, me):  # напоминалка в бою
        print(f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Fire Fang - Поджигает покемона противника\n"
              f"3) Protect - Устанавливает щит на покемона\n")



class Bulbosaur(Pokemon):
    def __init__(self):
        super(Bulbosaur, self).__init__()
        self.__type = "Grass"

    def get_type(self):
        return self.__type

    #Спешл атаки
    # Реализована перегрузка(мб не оч корректно)
    def Special1(self, me, enemy): #Poison Powder
        if enemy.get_status() != "Shield":
            enemy.set_status("Poison")
            enemy.set_timeEff(2)
            enemy.set_hp(enemy.get_hp() - 10)
            print(f"Покемон {enemy.get_name()} атакован. Он потерял 10 очков здоровья. Теперь его здоровье равно {enemy.get_hp()}\n"
                  f"Покемон {enemy.get_name()} отравлен\n"
                  f"Покемон {enemy.get_name()} потерял 2 очка здоровья. Теперь его здоровье равно {enemy.get_hp()}\n"
                  f"до снятия эффекта отравления осталось {enemy.get_timeEff()} ходов\n")


    #Задумка в том, что если противник уже "отравлен", то атака несет эффект вампиризма(отнимается здоровье у противника, в таком же объеме восстанавливается здоровье у себя)
    # + чуть выше урон(Очень ситуативна, но в этом и интерес)
    # Реализована перегрузка(мб не оч корректно)
    def Special2(self, me, enemy): #НЕ СООТВЕТСТВУЕТ ОПИСАНИЮ: Leech Seed
        if enemy.get_status() == "Poison":
            enemy.set_hp(enemy.get_hp() - 25)
            me.set_hp(me.get_hp() + 25)
            print(f"Покемон {enemy.get_name()} является отравленным.\n"
                  f"Покемон {enemy.get_name()} атакован. Он теряет 25 очков здоровья. Теперь его здоровье равно {enemy.get_hp()}\n"
                  f"Покемон {me.get_name()} восстанавливает 25 очков здоровья благодаря эффекту вамиризма. Теперь его здоровье равно {me.get_hp()}")
        else:
            print(f"Покемон {enemy.get_name()} не отравлен. Атака не имеет никакого эффекта")


    def tutorial(self, me):  # Стартовая инфа о выбранном классе покемона
        print(f"Вы выбрали покемона {me.get_name()}\n"
              f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Poison Powder - Отравляет покемона противника\n"
              f"3) Leech Seed - Если противник отравлен - повышенный урон + вампиризм\n")

    def fight_help(self, me):  # напоминалка в бою
        print(f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Poison Powder - Отравляет покемона противника\n"
              f"3) Leech Seed - Если противник отравлен - повышенный урон + вампиризм\n")



class Squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.__type = "Water"

    def get_type(self):
        return self.__type


    #Спешл атаки
    #Повышение базовой атаки на 5 + нанесение половины урона нового значения базовой атаки
    # Реализована перегрузка(мб не оч корректно)
    def Special1(self, me, enemy): #НЕ СООТВЕТСТВУЕТ ОПИСАНИЮ: Withdraw
        me.set_hit(me.get_hit() + 5)
        enemy.set_hp(enemy.get_hp() - (me.get_hit() // 2))
        print(f"Покемон {me.get_name()} повышает свою базовую атаку на 5 очков. Теперь его атака равна {me.get_hit()}\n"
              f"Покемон {me.get_name()} атакует покемона {enemy.get_name()} в пол силы\n"
              f"Покемон {enemy.get_name()} атакован. Он потерял {me.get_hit() // 2} hp. Теперь его здоровье равно {enemy.get_hp()}")


    #Покемон лечит 25 здоровья, но теряет 5 пунктов атаки
    #Балансится тем, что 5 атаки прибаваляются другой абилкой
    # Реализована перегрузка(мб не оч корректно)
    def Special2(self, me, enemy): #НЕ СООТВЕТСТВУЕТ ОПИСАНИЮ: Rain Dance
        if me.get_hit() > 5:
            me.set_hp(me.get_hp() + 25)
            me.set_hit(me.get_hit() - 5)
            print(f'Покемон {me.get_name()} восстанавливает 25 очков здоровья. Теперь его здоровье равно {me.get_hp()}\n'
                  f'Покемон {me.get_name()} теряет 5 очков атаки. Теперь его атака равна {me.get_hit()}')

    def tutorial(self, me):  # Стартовая инфа о выбранном классе покемона
        print(f"Вы выбрали покемона {me.get_name()}\n"
              f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Withdraw - Отравляет покемона противника\n"
              f"3) Leech Seed - Если противник отравлен - повышенный урон + вампиризм\n")

    def fight_help(self, me):  # напоминалка в бою
        print(f"Способности Покемона класса {me.get_name()}:\n"
              f"1) Обычная атака\n"
              f"2) Poison Powder - Повышение базовой атаки на 5 пунктов + нанесение половины урона нового значения базовой атаки\n"
              f"3) Rain Dance - Покемон лечит 25 здоровья, но теряет 5 пунктов атаки(Если значение атаки меньше 5, абилка тратится впустую)\n")

