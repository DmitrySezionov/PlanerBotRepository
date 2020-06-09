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
    bot.send_message(message.chat.id, '''Привет, я твой карманный помощник! Я много чего умею, поверь!
    \nДля того, чтобы начать со мной работать - <b>введи своё имя</b>, чтобы я зарегистрировал тебя!
    \nЕсли хочешь узнать, как я работаю, то загляни в команду /help.''', parse_mode='html')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'So, i didn`t know')

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling()