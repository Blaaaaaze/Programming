#Модуль исключений

#Базовое исключение. Наследуется от питоновского класса исключений
class Error(Exception):
    pass



#исключение некорректного ввода
class IncorrectInputExcError(Error):
    '''Некорректный ввод'''
    pass

class NoDataInBDError(Error):
    '''Таких данных нет в базе данных пользователей'''
    pass

class DublicateidError(Error):
    '''Указанный id уже существует'''
    pass

