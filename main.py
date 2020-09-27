import vk_api
import random
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

def write_msg(user_id, message):
    session.method('messages.send', {'user_id': user_id, 'message': message})
    
session = vk_api.VkApi(token='69a17e5303be5bc5218137622fa9684f6ac9b11d32f15c6b0b58cd3d1e1e8eee8ad89b443fb66c77d0c77')

#api = vk.get_api()
longpoll = VkBotLongPoll(session, 182437918)

print('Started!')


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            if event.message.text[0] == "!":

                print('MESSAGE WAS ARRIVED! ', event.message.text)

                session.method('messages.send', {'chat_id': event.chat_id, 'message': event.message.text, 'random_id': random.randint(0, 9999999999999999)})

                print('MESSAGE WAS SENDED!')