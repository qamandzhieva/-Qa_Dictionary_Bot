# В google colab добавить: !pip install pyTelegramBotAPI

import telebot
from telebot import types
import json
import random

bot = telebot.TeleBot(token="", parse_mode='html')

with open( "dict.json", "r", encoding="utf-8") as json_file:
    DEFINITIONS = json.load(json_file)

listDEFINITIONS = list(DEFINITIONS.values())

newDEFINITIONS = []

@bot.message_handler(commands=['start'])
def start_command_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Случайные термины✨随机词语')
    item2 = types.KeyboardButton('Кто тебя создал/谁开发了你？')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!  Я помогу тебе разобраться с основными понятиями и аббревиатурами, которые помогут тебе глубже погрузиться в работу на площадке🤓 哈喽，我将帮助您理解主要词语并简称，这将帮助您更深地理解网站上的工作🤓  \nВведи интересующий термин, например,/请输入感兴趣的词语或简称，例如，<u><b>FBS</b></u>", parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.text != "Случайные термины✨随机词语" and message.text != "Кто тебя создал/谁开发了你？":
        definition = DEFINITIONS.get(message.text.lower())
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Случайные термины✨随机词语')
        item2 = types.KeyboardButton('Кто тебя создал/谁开发了你？')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, text=f'Определение 该词语的意思:\n<code>{definition}</code>')
        bot.send_message(message.chat.id, text=f'Хочешь узнать что нибудь другое/想知道其他词的意思吗？', reply_markup=markup)
        if definition is None and message.text != "Случайные термины✨随机词语" and message.text != "Кто тебя создал/谁开发了你?":
            newDEFINITIONS.append(message.text)
            with open('newdict.txt', "a", encoding="utf-8") as txt_file:
                print(*newDEFINITIONS, file=txt_file, sep="\n")
            bot.send_message(message.chat.id, f'Кажется, этого определения у меня ещё нет🤔好像我不知道这个词语\nЯ добавлю термин 我添加该词, 将一定会知道这个词的意思<u><b>{message.text}</b></u> в свой список и обязательно узнаю что это такое🤓')

    elif message.text == "Случайные термины✨随机词语":
        bot.send_message(message.chat.id, random.choice(listDEFINITIONS))
        bot.send_message(message.chat.id, random.choice(listDEFINITIONS))
        bot.send_message(message.chat.id, random.choice(listDEFINITIONS))
        bot.send_message(message.chat.id, random.choice(listDEFINITIONS))
        bot.send_message(message.chat.id, random.choice(listDEFINITIONS))

    elif message.text == "Кто тебя создал/谁开发了你？":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Сайт-визитка', url='https://qamandzhieva.github.io')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Тебе правда интересно?☺ Переходи по ссылке!'.format(message.from_user), reply_markup=markup)

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
