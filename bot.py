import re
import telebot

TOKEN = '1297554794:AAHuCSd-vol-lOPPOcBqhjdGihWgIW719sU'
bot = telebot.TeleBot(TOKEN)

keyboard_start = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_start.row('My Tasks', 'Add new task', 'Settings')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, i`m Planer Bot. Use me, to create notifications', reply_markup=keyboard_start)



#MY TASK
def correct_text1(sentence):
    is_correct = re.match(r'^[My Tasks]+$', sentence)
    return bool(is_correct)

def preprocess_text1(sentence):
    sentence = re.sub(r'\W+', '', sentence.lower().strip())  # Delete special symbols
    sentence = re.sub(r'([a-z])\1+', r'\1', sentence)  # Remove duplicates
    return sentence



#ADD NEW TASK
# def correct_text2(sentence):
#     is_correct = re.match(r'^[Add new task]+$', sentence)
#     return bool(is_correct)
#
# def preprocess_text2(sentence):
#     sentence = re.sub(r'\W+', '', sentence.lower().strip())  # Delete special symbols
#     sentence = re.sub(r'([a-z])\1+', r'\1', sentence)  # Remove duplicates
#     return sentence




@bot.message_handler(content_types=['text'])
def mytask_text(message):
    cid = message.chat.id

    if correct_text1(preprocess_text1(message.text)):
        bot.send_message(message.chat.id, '''Your task today:
        \nIf you want to view all task, choose from menu.''', reply_markup=keyboard_add)
    else:
        bot.send_message(message.chat.id, 'I don`t know that')

    # if correct_text1(preprocess_text1(message.text)):
    #     bot.send_message(message.chat.id, 'Your tasks', reply_markup=keyboard_add)
    # elif correct_text2(preprocess_text2(message.text)):
    #     bot.send_message(message.chat.id, 'Put your task name')
    # else:
    #     bot.send_message(message.chat.id, 'NONONON')



if __name__ == '__main__':
    bot.polling()