class VkBot:

    def __init__(self):
        self._COMMANDS = [[['что умеешь', 'хелп', 'помощь']], "U gay"]

    def new_message(self, message):
        '''Чекер сообщений

        :param message: текст сообщения
        :type message: str

        '''

        for c in self._COMMANDS[0]:
            for m in c:
                if message.lower() == m: return '''Краткий экскурс по командам:'''

        if message.lower() == self._COMMANDS[1]:
            return "No u"

        else: return message


        