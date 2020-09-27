class VkBot:

    def __init__(self):
        self._COMMANDS = ["Ты гей", "U gay"]

    def new_message(self, message):
        '''Чекер сообщений

        :param message: текст сообщения
        :type message: str

        '''

        if message == self._COMMANDS[0]:
            return "Нет, ты"

        elif message == self._COMMANDS[1]:
            return "No u"

        else: return f'''Нахуй ты мне пишешь "{message}"?
        Пиздуй лучше доделывать меня🔫
        '''


        