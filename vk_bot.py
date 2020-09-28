import money

class VkBot:
    
    def __init__(self):
        self._COMMANDS = [['что умеешь', 'хелп', 'помощь', 'help'], ['бал', 'балланс', 'деньги', 'bal', 'money', 'balance'], 'ты гей']

    def new_message(self, message):
        '''Чекер сообщений

        :param message: текст сообщения
        :type message: str

        '''
        
        if message.lower() in self._COMMANDS[0]: 
            return '''Краткий экскурс по командам:
            /хелп - выводит список всех команд
            /баланс - выводит денежный счёт пользователя
            '''       

        if message.lower() in self._COMMANDS[1]:
            return f'Ваш баланс составляет  республиканских стафила'

        if message.lower() in self._COMMANDS[2]:
            return 'А может быть ты?'