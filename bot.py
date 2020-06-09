# -*- coding: utf-8 -*-
import re
import telebot
import config

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, i`m Planer Bot. Use me, to create notifications')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'So, i didn`t know')

if __name__ == '__main__':
    bot.polling()