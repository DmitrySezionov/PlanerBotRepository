import re
import telebot

TOKEN = '1297554794:AAHuCSd-vol-lOPPOcBqhjdGihWgIW719sU'
bot = telebot.TeleBot(TOKEN)

keyboard1 = keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Add new task', 'My Tasks', 'Settings')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, i`m Planer Bot. Use me, to create notifications', reply_markup=keyboard1)

def correct_text1(sentence):
    is_correct = re.match(r'^[add new task]+$', sentence)
    return bool(is_correct)

def preprocess_text1(sentence):
    sentence = re.sub(r'\W+', '', sentence.lower().strip())  # Delete special symbols
    sentence = re.sub(r'([a-z])\1+', r'\1', sentence)  # Remove duplicates
    return sentence

@bot.message_handler(content_types=['text'])
def add_text(message):
    cid = message.chat.id

    if correct_text1(preprocess_text1(message.text)):
        bot.send_message(message.chat.id, 'yeyes')
    else:
        bot.send_message(message.chat.id, 'NONONON')

if __name__ == '__main__':
    bot.polling()