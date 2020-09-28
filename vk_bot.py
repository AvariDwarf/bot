from currency import Currency


class VkBot:
    
    def __init__(self):
        self._COMMANDS = [['что умеешь', 'хелп', 'помощь', 'help'], ['курс', 'валюта',]]

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


        if message.lower() in self._COMMANDS[1]:

            cur = Currency()

            return f'''
            Курс валют на {cur.TIME}:
            
            Российский рубль - {cur.RUB} ₽
            Белорусский рубль - {cur.BYN} Br
            Евро - {cur.EUR} €
            Биткоин - {cur.BTC} ₿
            Республиканский стафил - {cur.RSF} ŘŞ
            '''


        