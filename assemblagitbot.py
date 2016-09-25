import datetime
import random
import time

import assembla
import telepot

import configuration


def getUsersListAnswer(msg):
    space = assembla.spaces(name=configuration.assembla_space)[0]
    users = space.users()
    print(users)
    user_strlist = ''
    for u in users:
        try:
            email = u.data['email']
        except KeyError:
            email = 'none@foo.bar'
        user_strlist += u.data['name'] + ' (' + u.data['login'] + ') ' + email + '\n'

    message = 'С репозиторием ' + '"' + configuration.assembla_space + '"' + \
              ' сейчас могут работать: \n' + \
              user_strlist

    return message


def getHelpMessage(msg):
    message = 'Привет! Я AssemblaGitBot! \n' \
              'Вот мои доступные команды: \n' \
              '/users - пользователи репозитория "' + configuration.assembla_space + '"\n' \
                                                                                     '/roll - получить случайное число от 1 до 100\n' \
                                                                                     '/time - возвращает некущую дату и время\n' \
                                                                                     '/getanswer - ответ на «Главный вопрос жизни, вселенной и всего такого»\n' \
                                                                                     '/help - это сообщение\n' \
                                                                                     '\n' \
                                                                                     'Have a nice day! :)\n' \
                                                                                     '\n' \
                                                                                     'by @volodink'
    return message


def handle(msg):
    chat_id = msg['chat']['id']

    user_id = msg['from']['id']

    if user_id in configuration.allowed_users:
        command = msg['text']

        print('Got command: %s' % command)
        print('User: %s' % user_id)

        if command == '/roll':
            bot.sendMessage(chat_id, random.randint(1, 100))

        elif command == '/time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))

        elif command == '/getanswer':
            bot.sendMessage(chat_id, str(42))

        elif command == '/users':
            message = getUsersListAnswer(msg)
            bot.sendMessage(chat_id, message)

        elif command == '/help':
            message = getHelpMessage(msg)
            bot.sendMessage(chat_id, message)
    else:
        print('User: %s' % user_id)
        bot.sendMessage(chat_id, 'Сорян, чувак, но тебя нет в списке.\nОбратись к разработчику: @volodink')


bot = telepot.Bot(configuration.telegram_bot_token)

bot.message_loop(handle)

print('Listening ...')

print('Creating Assembla object ...')

assembla = assembla.API(key=configuration.assembla_userKey, secret=configuration.assembla_secretKey)


# Keep the program running.
while 1:
    time.sleep(5)
