import fighters
import time





class Fight:


    #Пик покемонов
    def take_pokemon(self):
        while True: #Добивается правильного ввода
            first_pick = input("Выберите покемона:\n"
                               "1) Пикачу\n"
                               "2) Чармандер\n"
                               "3) Бульбозавр\n"
                               "4) Сквиртл\n")
            # Насколько я понимаю, в этом if-elif-else реализована композиция
            if first_pick == '1':
                poke1 = fighters.Pikachu()
                poke1.set_name("Pikachu")
                poke1.tutorial(poke1)
                break
            elif first_pick == '2':
                poke1 = fighters.Charmander()
                poke1.set_name("Charmander")
                poke1.tutorial(poke1)
                break
            elif first_pick == '3':
                poke1 = fighters.Bulbosaur()
                poke1.set_name("Bulbosaur")
                poke1.tutorial(poke1)
                break
            elif first_pick == '4':
                poke1 = fighters.Squirtle()
                poke1.set_name("Squirtle")
                poke1.tutorial(poke1)
                break
            else:
                print("Некорректный ввод")

        while True: #Добивается правильного ввода
            second_pick = input("Выберите покемона:\n"
                               "1) Пикачу\n"
                               "2) Чармандер\n"
                               "3) Бульбозавр\n"
                               "4) Сквиртл\n")
            #Насколько я понимаю, в этом if-elif-else реализована композиция
            if second_pick == '1':
                poke2 = fighters.Pikachu()
                poke2.set_name("Pikachu")
                poke2.tutorial(poke2)
                break
            elif second_pick == '2':
                poke2 = fighters.Charmander()
                poke2.set_name("Charmander")
                poke2.tutorial(poke2)
                break
            elif second_pick == '3':
                poke2 = fighters.Bulbosaur()
                poke2.set_name("Bulbosaur")
                poke2.tutorial(poke2)
                break
            elif second_pick == '4':
                poke2 = fighters.Squirtle()
                poke2.set_name("Squirtle")
                poke2.tutorial(poke2)
                break
            else:
                print("Некорректный ввод")

        return [poke1, poke2]  #возвращает массив из двух выбранных покемонов (они могут быть и одинаковыми - это нормально)


    def use_pokemon(self, poke, enemy): #функция на использование абилок покемона
        while True:
            move = input('Введите порядковый номер атаки: ')
            if move == '1':
                poke.attack(poke, enemy)
                break
            elif move == '2':
                poke.Special1(poke, enemy)
                break
            elif move == '3':
                poke.Special2(poke, enemy)
                break
            else:
                print("Неверный ввод")


    #Битва покемонов
    def Battle(self):
        #В следующих 3 строках (80, 81, 82) обозначаются выбранные бойцы-покемоны
        massive = Fight.take_pokemon(self)
        warrior1 = massive[0]
        warrior2 = massive[1]
        count = 1 # будет определять порядок ходов

        #Бой идет
        while True: #Продолжительность битвы
            attack = count%2 #порядок ходов определяется остатком номера хода при делении на 2
            count+=1 #счетчик ходов, при пропуске хода он не собьется
            #Действия первого
            if attack == 1:
                print(f'Ход покемона {warrior1.get_name()}')
                warrior1.check_my_status() #Проверка на эффекты
                if warrior1.get_PossMove() == 1: #Если не оглушен
                    warrior1.fight_help(warrior1) #напоминание куда жмякать

                    Fight.use_pokemon(self, warrior1, warrior2) #Выбор действия покемона, реализация выбранного способности
                else:
                    print(f"Покемон {warrior1.get_name()} пропускает ход")

            #Действия второго
            else:
                print(f'Ход покемона {warrior2.get_name()}')
                warrior2.check_my_status() #Проверка на эффекты
                if warrior2.get_PossMove() == 1: #Если не оглушен
                    warrior2.fight_help(warrior2) #подсказка по способностям
                    Fight.use_pokemon(self, warrior2, warrior1) #Выбор действия покемона, реализация выбранного способности
                else:
                    print(f"Покемон {warrior2.get_name()} пропускает ход")

            #Отслеживать конец
            if warrior1.get_hp() <= 0: #У первого покемона закончилось hp
                print(f"Покемон {warrior1.get_name()} проиграл")
                exit()
            if warrior2.get_hp()  <= 0: # у второго покемона закончилось hp
                print(f"Покемон {warrior2.get_name()} проиграл")
                exit()


# Fight.Battle()