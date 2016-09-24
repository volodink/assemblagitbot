import telepot

import random
import time
import datetime

import configuration

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1, 100))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/getanswer':
        bot.sendMessage(chat_id, str(42))
    elif command == '/help':
        d = 'Привет! Я AssemblaGitBot! \n' \
            'Вот мои доступные команды: \n' \
            '/roll - получить случайное число от 1 до 100\n' \
            '/time - возвращает некущую дату и время\n' \
            '/getanswer - ответ на «Главный вопрос жизни, вселенной и всего такого»\n' \
            '/help - это сообщение\n' \
            '\n' \
            'Have a nice day! :)\n' \
            '\n' \
            'by @volodink'
        bot.sendMessage(chat_id, str(d))


bot = telepot.Bot(configuration.TOKEN)
bot.message_loop(handle)
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)