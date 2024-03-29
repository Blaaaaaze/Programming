#Модуль исключений

#Базовое исключение. Наследуется от питоновского класса исключений
class Error(Exception):
    pass



#исключение некорректного ввода
class IncorrectInputExcError(Error):
    '''Некорректный ввод'''
    pass

#Исключение вместо флага состояния
class CantTurnError(Error):
    '''Невозможность сделать ход (активный эффект оглушения)'''
    pass


#Неудачная попытка перехвата игры НЕ человека. Пока не используется нигде
class BotTurnError(Error):
    '''Если играет бот, а не человек'''
    pass