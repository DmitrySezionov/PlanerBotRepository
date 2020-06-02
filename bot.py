import re
import telebot

TOKEN = '1297554794:AAHuCSd-vol-lOPPOcBqhjdGihWgIW719sU'
bot = telebot.TeleBot(TOKEN)

keyboard_start = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_start.row('Add new task', 'My Tasks', 'Settings')

keyboard_add = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_add.row('Task Today', 'All Tasks')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, i`m Planer Bot. Use me, to create notifications', reply_markup=keyboard_start)




def correct_text1(sentence):
    is_correct = re.match(r'^[My Task]+$', sentence)
    return bool(is_correct)

def preprocess_text1(sentence):
    sentence = re.sub(r'\W+', '', sentence.lower().strip())  # Delete special symbols
    sentence = re.sub(r'([a-z])\1+', r'\1', sentence)  # Remove duplicates
    return sentence




def correct_text2(sentence):
    is_correct = re.match(r'^[Add new task]+$', sentence)
    return bool(is_correct)

def preprocess_text2(sentence):
    sentence = re.sub(r'\W+', '', sentence.lower().strip())  # Delete special symbols
    sentence = re.sub(r'([a-z])\1+', r'\1', sentence)  # Remove duplicates
    return sentence




@bot.message_handler(content_types=['text'])
def add_text(message):
    cid = message.chat.id

    if correct_text1(preprocess_text1(message.text)):
        bot.send_message(message.chat.id, 'Your tasks')
    elif correct_text2(preprocess_text2(message.text)):
        bot.send_message(message.chat.id, 'Put your task name', reply_markup=keyboard_add)
    else:
        bot.send_message(message.chat.id, 'NONONON')

if __name__ == '__main__':
    bot.polling()