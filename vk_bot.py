from currency import Currency


class VkBot:
    
    def __init__(self):
        self._COMMANDS = [['что умеешь', 'хелп', 'помощь', 'help']]

    def new_message(self, message):
        '''Чекер сообщений

        :param message: текст сообщения
        :type message: str

        '''
        
        if message.lower() in self._COMMANDS[0]: 
            return '''Краткий экскурс по командам:
            /хелп - выводит 
            /курс - выводит курсы валют относительно одного доллара США по данным Google
            '''       