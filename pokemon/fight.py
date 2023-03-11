import fighters


#Пик покемонов
def take_pokemon():
    while True: #Добивается правильного ввода
        first_pick = input("Выберите покемона:\n"
                           "1) Пикачу\n"
                           "2) Чармандер\n"
                           "3) Бульбозавр\n"
                           "4) Сквиртл\n")
        if first_pick == '1':
            poke1 = fighters.Pikachu()
            poke1.set_name("Pikachu")
            break
        elif first_pick == '2':
            poke1 = fighters.Charmander()
            poke1.set_name("Charmander")
            break
        elif first_pick == '3':
            poke1 = fighters.Bulbosaur()
            poke1.set_name("Bulbosaur")
            break
        elif first_pick == '4':
            poke1 = fighters.Squirtle()
            poke1.set_name("Squirtle")
            break
        else:
            print("Некорректный ввод")

    while True: #Добивается правильного ввода
        second_pick = input("Выберите покемона:\n"
                           "1) Пикачу\n"
                           "2) Чармандер\n"
                           "3) Бульбозавр\n"
                           "4) Сквиртл\n")
        if second_pick == '1':
            poke2 = fighters.Pikachu()
            poke2.set_name("Pikachu")
            break
        elif second_pick == '2':
            poke2 = fighters.Charmander()
            poke2.set_name("Charmander")
            break
        elif second_pick == '3':
            poke2 = fighters.Bulbosaur()
            poke2.set_name("Bulbosaur")
            break
        elif second_pick == '4':
            poke2 = fighters.Squirtle()
            poke2.set_name("Squirtle")
            break
        else:
            print("Некорректный ввод")

    return [poke1, poke2]  #возвращает массив из двух покемонов

def use_pokemon(poke, enemy): #функция на использование абилок покемона
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
def Battle():
    massive = take_pokemon()
    warrior1 = massive[0]
    warrior2 = massive[1]
    count = 1 # будет определять порядок ходов

    #Бой идет
    while True: #Продолжительность битвы
        attack = count%2 #порядок ходов определяется остатком номера хода при делении на 2
        count+=1
        #Действия первого
        if attack == 1:
            print(f'Ход покемона {warrior1.get_name()}')
            warrior1.check_my_status() #Проверка на эффекты
            if warrior1.get_PossMove() == 1: #Если не оглушен
                warrior1.fight_help(warrior1) #напоминание куда жмякать
                use_pokemon(warrior1, warrior2)
            else:
                print(f"Покемон {warrior1.get_name()} пропускает ход")

        #Действия второго
        else:
            print(f'Ход покемона {warrior2.get_name()}')
            warrior2.check_my_status() #Проверка на эффекты
            if warrior2.get_PossMove() == 1: #Если не оглушен
                warrior2.fight_help(warrior2) #подсказка по способностям
                use_pokemon(warrior2, warrior1)
            else:
                print(f"Покемон {warrior2.get_name()} пропускает ход")

        #Отслеживать конец
        if warrior1.get_hp() <= 0:
            print(f"Покемон {warrior1.get_name()} проиграл")
            exit()
        if warrior2.get_hp()  <= 0:
            print(f"Покемон {warrior2.get_name()} проиграл")
            exit()


Battle()