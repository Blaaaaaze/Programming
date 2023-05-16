from Cars import *
from Exceptions import *
import re
import sqlite3
import datetime


class BD: #класс для методов работы с бд
    def view_BD(self, numb_of_table): #Получение всех данных из БД
        try:
            connection = sqlite3.connect('AllBD.db')
            cur = connection.cursor()
            if numb_of_table == 1:
                m = cur.execute("""SELECT * FROM tUsers""")
                all_values = list(m.fetchall())
            elif numb_of_table == 2:
                m = cur.execute("""SELECT * FROM tCars""")
                all_values = list(m.fetchall())
            elif numb_of_table == 3:
                m = cur.execute("""SELECT * FROM tOrders""")
                all_values = list(m.fetchall())
            cur.close()
            return all_values
        except sqlite3.Error as error:
            print('Ошибка при получении данных из базы данных', error)
        finally:
            if (connection):
                connection.commit()
                connection.close()


    def BD_update(self, name, password, admin): #Запись данных нового аккаунта
        try:
            connection = sqlite3.connect('AllBD.db')
            cur = connection.cursor()
            new_item = (name, password, admin)
            cur.execute("""INSERT INTO tUsers Values (?, ?, ?)""", new_item)
            cur.close()
        except sqlite3.Error as error:
            print('Ошибка при подключение SQLite', error)
        finally:
            if (connection):
                connection.commit()
                connection.close()

    def BD_check(self, name, password, admin): #Проверка нахождения аккаунта в БД
        conection = sqlite3.connect('AllBD.db')
        cur = conection.cursor()
        users = cur.execute("""SELECT * FROM tUsers""")
        for i in users:
            if name == str(i[0]) and password == int(i[1]) and admin == int(i[2]):
                cur.close()
                return 1
        cur.close()
        conection.close()
        return 0

    def car_bd(self, new_item): #Добавление новой машины в БД
        try:
            connection = sqlite3.connect('AllBD.db')
            cur = connection.cursor()
            # if flag == 1:
            cur.execute("""INSERT INTO tCars Values (?, ?, ?, ?, ?, ?, ?)""", new_item)
            # else:
            #     cur.execute("""DELETE FROM tCars WHERE id=?""", new_item)
            cur.close()
        except sqlite3.Error as error:
            print('При сохранении автомобиля произошла ошибка', error)
        finally:
            if (connection):
                print('Новый автомобиль успешно добавлен в базу')
                connection.commit()
                connection.close()

    def car_del(self, id_of_car): #Удаление машины из базы
        try:
            connection = sqlite3.connect('AllBD.db')
            cur = connection.cursor()
            cur.execute("""DELETE FROM tCars WHERE id=?""", (id_of_car,))
            cur.close()
        except sqlite3.Error as error:
            print('При сохранении автомобиля произошла ошибка', error)
        finally:
            if (connection):
                print('Автомобиль успешно удален из базы')
                connection.commit()
                connection.close()

    def add_offer(self, offer):
        try:
            connection = sqlite3.connect('AllBD.db')
            cur = connection.cursor()
            cur.execute("""INSERT INTO tOrders Values (?, ?, ?, ?)""", offer)
            cur.close()
            cur1 = connection.cursor()
            if offer[2] == 'Бронирование':
                cur1.execute("""UPDATE tCars set Busy=2 where id=?""", (int(offer[1]),))
            else:
                cur1.execute("""UPDATE tCars set Busy=1 where id=?""", (int(offer[1]),))
            cur1.close()
        except sqlite3.Error as error:
            print('При сохранении заказа произошла ошибка', error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print('Новый заказ успешно оформлен')


    def delete_by_time(self):
        try:
            connection = sqlite3.connect('AllBD.db')
            list_of_offers = self.view_BD(3)
            for i in range(len(list_of_offers)):
                if self.normal_vid(datetime.datetime.now()) >= self.normal_vid(list_of_offers[i][-1]):
                    cur = connection.cursor()
                    cur.execute("""DELETE FROM tOrders WHERE end_datetime=?""",(list_of_offers[i][-1],))
                    cur.close()
                    cur1 = connection.cursor()
                    cur1.execute("""UPDATE tCars set Busy=0 where id=?""", (int(list_of_offers[i][1]),))
                    cur1.close()
        except sqlite3.Error as error:
            print('Ошибка проверки заказов', error)
        finally:
            if (connection):
                print('Появился новый свободный автомобиль')
                connection.commit()
                connection.close()

    def normal_vid(self, time):
        time = str(time)
        stroka = ''
        for i in time:
            if i in '1234567890':
                stroka += i
        return stroka

class Menu(BD):
    #Основной блок
    #метод для выполнения входа в аккаунты или создание нового
    def log_in(self, admin, first):#принимает 2 параметра: Если admin = 1, то проверка по графе админов, 0 - по обычной; first = 1 - добавление новых данных в бд, 0 - обычный вход, проверка по таблице пользователей
            global name
            try:
                while True:
                    print(f'В имени только буквы английского афлавита в обоих регистрах\n'
                          f'В пароле только цифры\n'
                          f'Чтобы выйти обратно в меню, введите две пустых строки')

                    self.name = input('Введите имя пользователя: ')
                    password = input('Введите пароль: ')
                    r = re.compile(r'[a-zA-Z]+')
                    if not r.match(self.name) or password.isnumeric() == False:
                        raise IncorrectInputExcError
                    break
                password = int(password)
                if first == 0:
                    if self.BD_check(self.name, password, admin) == 0:
                        raise NoDataInBDError
                    if admin == 0:
                        self.main_menu()
                    else:
                        self.admin_menu()
                else:
                    self.BD_update(self.name, password, admin)
                    return
            except IncorrectInputExcError:
                print('Неправильный ввод, повторите попытку')
            except NoDataInBDError:
                print('Такого пользователя нет, повторите попытку')




    def first_menu(self): #меню логина
        first_command = ['Войти', 'Войти как администратор','Зарегистрироваться', 'Выйти из системы']
        for i in range(len(first_command)):
            print(i+1, first_command[i])
        while True:
            move = input('Введите номер команды: ')
            if move == '1':
                self.delete_by_time()
                self.log_in(0, 0)
            elif move == '2':
                self.delete_by_time()
                self.log_in(1, 0)
            elif move == '3':
                self.delete_by_time()
                self.log_in(0, 1)
            elif move == '4':
                self.delete_by_time()
                exit()


    def main_menu(self): #основное меню
        while True:
            commands = ['Просмотреть весь доступный транспорт', 'Просмотреть весь свободный транспорт', 'Просмотреть транспорт по грузоподъёмности', 'Создать новую заявку на перевоз', 'Подобрать и забронировать транспорт', 'Выйти из аккаунта', 'Выйти из системы']
            for i in range(len(commands)):
                print(i+1, commands[i])
            pick = input('Введите номер команды')
            if pick == '1':
                self.view_all_cars()
                self.delete_by_time()
                self.main_menu()
            elif pick == '2':
                self.view_free_cars()
                self.delete_by_time()
                self.main_menu()
            elif pick == '3':
                self.sort_cars()
                self.delete_by_time()
                self.main_menu()
            elif pick == '4':
                self.New_offer()
                self.delete_by_time()
                self.main_menu()
            elif pick == '5':
                self.check_car_by_parametres()
                self.delete_by_time()
                self.main_menu()
            elif pick == '6':
                self.delete_by_time()
                print('Вы вышли из аккаунта')
                self.first_menu()
            elif pick == '7':
                self.delete_by_time()
                print('Вы вышли из системы')
                exit()
            else:
                self.delete_by_time()
                print('Неправильный ввод! Повторите попытку')

    def admin_menu(self): #Основное меню, для админов
        commands = ['Добавить транспорт', 'Удалить транспорт', 'Просмотреть весь доступный транспорт',
                    'Просмотреть весь свободный транспорт', 'Просмотреть транспорт по грузоподъёмности',
                    'Создать новую заявку на перевоз', 'Подобрать и забронировать транспорт', 'Выйти из аккаунта',
                    'Выйти из системы']
        for i in range(len(commands)):
            print(i + 1, commands[i])
        pick = input('Введите номер команды')
        if pick == '1':
            self.add_car()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '2':
            self.del_car()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '3':
            self.view_all_cars()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '4':
            self.view_free_cars()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '5':
            self.sort_cars()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '6':
            self.New_offer()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '7':
            self.check_car_by_parametres()
            self.delete_by_time()
            self.admin_menu()
        elif pick == '8':
            print('Вы вышли из аккаунта')
            self.delete_by_time()
            self.first_menu()
        elif pick == '9':
            print('Вы вышли из системы')
            self.delete_by_time()
            exit()
        else:
            print('Неправильный ввод! Повторите попытку')
            self.delete_by_time()

    def add_car(self): #кнопка - добавить автомобиль
        while True:
            try:
                types_of_car = ['ГАЗ-3302 «Газель»', 'ЗИЛ-5301 (Бычок)', 'MAN-10', 'Фура Mercedes-Benz Actros']
                print('Доступные модели машин')
                for i in range(len(types_of_car)):
                    print(i+1, types_of_car[i])
                turn = input('Выберите тип автомобиля')
                numbers = input('Введите id автомобиля')
                if numbers.isnumeric() == False:
                    raise IncorrectInputExcError
                if turn == '1':
                    new_car = Gazel(numbers)
                elif turn == '2':
                    new_car = Bull(numbers)
                elif turn == '3':
                    new_car = MAN(numbers)
                elif turn =='4':
                    new_car = Truck(numbers)
                else:
                    print('Неправильный ввод! Повторите попытку')
                break
            except IncorrectInputExcError:
                print('Некорретные данные, повторите попытку')
        car_add = (new_car.get_name(), new_car.get_id(), new_car.get_length(), new_car.get_width(), new_car.get_height(), new_car.get_LeftCap(), 0)
        self.car_bd(car_add)
        return

    def del_car(self): #кнопка - удалить автомобиль
        list_of_car = self.view_BD(2)
        for i in range(len(list_of_car)):
            print(i+1, list_of_car[i])
        while True:
            try:
                delete = input('Введите номер машины, которую надо удалить')
                if delete.isnumeric() == False:
                    raise IncorrectInputExcError
                else:
                    if int(delete) > len(list_of_car):
                        raise IncorrectInputExcError
            except IncorrectInputExcError:
                print('Некорректный ввод')
            break

        self.car_del(list_of_car[int(delete)-1][1])


    def view_all_cars(self): #Просмотр всего имеющегося транспорта
        list_of_all_cars = self.view_BD(2)
        for i in list_of_all_cars:
            print(i)

    def view_free_cars(self): #просмотр свободных машин
        list_of_free_cars = self.view_BD(2)
        list_of_offers = self.view_BD(3)
        free_cars = []
        for i in list_of_free_cars:
            for j in list_of_offers:
                if i[-1] == 0 or (i[-1] == 2 and j[0] == self.name and i[1]==j[1]):
                    free_cars.append(i)
        free_cars = set(free_cars)
        for i in free_cars:
            print(i)

    def sort_cars(self): #Показ машин по грузоподъемности
        list_of_types_cars = ['ГАЗ-3302 «Газель»', 'ЗИЛ-5301 (Бычок)', 'MAN-10', 'Фура Mercedes-Benz Actros']
        inp = input('Введите 1, чтобы посмотреть список автомобилей в порядке возрастания грузоподьемности\n'
                    'Введите 2, чтобы посмотреть список автомобилей в порядке убывания грузоподьемности\n')
        while True:
            if inp == '1':
                for i in range(len(list_of_types_cars)):
                    print(list_of_types_cars[i])
                break
            elif inp == '2':
                for i in range(len(list_of_types_cars), -1, -1):
                    print(list_of_types_cars[i])
                break
            else:
                print('Неверный ввод! попробуй еще раз')


    def New_offer(self):
        offer_LeftCap = int(input('Введите вес груза'))
        offer_length = int(input('Введите длину груза'))
        offer_width = int(input('Введите ширину груза'))
        offer_height = int(input('Введите высоту груза'))
        offer_name = input('Введите название груза')
        end_time = input('Введите дату и время приема заказа через пробел в формате: год-месяц-день час:минуты')
        '''В будущем поставить проверку на цифры'''
        good_cars = []
        list_of_cars_for_offer = self.view_BD(2)
        for i in range(len(list_of_cars_for_offer)):
            if list_of_cars_for_offer[i][-1] != 1:
                if offer_LeftCap <= list_of_cars_for_offer[i][5] and offer_length <= list_of_cars_for_offer[i][2] and offer_width <= list_of_cars_for_offer[i][3] and offer_height <= list_of_cars_for_offer[i][4]:
                    good_cars.append(list_of_cars_for_offer[i])
        if len(good_cars) != 0:
            print('Подходящие машины')
            for i in range(len(good_cars)):
                print(good_cars[i])
            while True:
                check_True = 0
                take_car = input('Введите id подходящей машины')
                for i in range(len(good_cars)):
                    if take_car == str(good_cars[i][1]):
                        print('Продолжаем работу над заказом')
                        check_True = 1
                        break
                if check_True == 1:
                    break
            full_date = end_time.split(' ')
            new_offer = (self.name, take_car, offer_name, datetime.datetime(int(full_date[0]), int(full_date[1]), int(full_date[2]), int(full_date[3]), int(full_date[4])))
            self.add_offer(new_offer)

        else:
            print('К сожалению, подходящих машин сейчас нет или они находятся в рейсе')


    def check_car_by_parametres(self):
        offer_LeftCap = int(input('Введите вес груза'))
        offer_length = int(input('Введите длину груза'))
        offer_width = int(input('Введите ширину груза'))
        offer_height = int(input('Введите высоту груза'))
        list_of_cars_for_check = self.view_BD(2)
        best_parametres = [10000000000000, 10000000000000, 10000000000000, 10000000000000, 'FFF']#длина ширина высота тяжесть
        for i in range(len(list_of_cars_for_check)):
            if list_of_cars_for_check[i][-1] != 1:
                if offer_LeftCap <= list_of_cars_for_check[i][5] and offer_length <= list_of_cars_for_check[i][2] and offer_width <= list_of_cars_for_check[i][3] and offer_height <= list_of_cars_for_check[i][4]:
                    if best_parametres[0] >= list_of_cars_for_check[i][2] and best_parametres[1] >= list_of_cars_for_check[i][3] and best_parametres[2] >= list_of_cars_for_check[i][4] and best_parametres[3] >= list_of_cars_for_check[i][5]:
                        best_parametres = [list_of_cars_for_check[i][2], list_of_cars_for_check[i][3], list_of_cars_for_check[i][4], list_of_cars_for_check[i][5], list_of_cars_for_check[i][0]]

        if best_parametres[-1] == 'FFF':
            print('В данный момент нет подходящей машины')
        else:
            print(f'Вам подходит автомобиль: {best_parametres[-1]}'
                  f'Все доступные машины данные модели:')
            for i in range(len(list_of_cars_for_check)):
                if best_parametres[-1] == list_of_cars_for_check[i][0] and list_of_cars_for_check[i][-1] != 1:
                    print(list_of_cars_for_check[i])
            move = input('Хотите забронировать автомобиль?')
            if move == 'нет':
                return
            else:
                take_car = input('Введите id подходящей машины')
                booking_offer = (self.name, take_car, 'Бронирование', datetime.datetime.now() + datetime.timedelta(days=3))
                self.add_offer(booking_offer)




v = Menu()
v.first_menu()