import re
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, i`m Planer Bot. Use me, to create notifications')


if __name__ == '__main__':
    bot.polling()