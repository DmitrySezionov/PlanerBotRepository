# -*- coding: utf-8 -*-
import re
import telebot
import os
import config

TOKEN = '1297554794:AAHuCSd-vol-lOPPOcBqhjdGihWgIW719sU'
bot = telebot.TeleBot(TOKEN)

user_data = {}

class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.age = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, '''Привет, я твой карманный помощник! Я много чего умею, поверь!
    \nДля того, чтобы начать со мной работать - <b>введи своё имя</b>, чтобы я зарегистрировал тебя!''', parse_mode='html')
    bot.register_next_step_handler(msg, process_first_name_step)

def process_first_name_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, 'Отлично, а теперь введи Фамилию!')
        bot.register_next_step_handler(msg, process_last_name_step)
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то пошло не так...')

def process_last_name_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text
        bot.send_message(message.chat.id, 'Регистрация успешна!')
    except Exception as e:
        bot.send_message(message.chat.id, 'Что-то явно пошло не так?')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'So, i didn`t know')

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling()