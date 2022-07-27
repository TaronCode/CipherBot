import telebot
from telebot import types
from auth_data import token
from auth_data import Cipher
from auth_data import disCipher
cip = 2
step = 1
step_true = 0
def telegram_bot(token):
    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/Шифровать")
        btn2 = types.KeyboardButton("/Дэшифровать")
        btn3 = types.KeyboardButton("/Шаг")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Привет! Здесь ты можеш зашифровать свой текст шифром цезаря", reply_markup=markup)

    @bot.message_handler(commands=["Шифровать"])
    def ciphering_mode(message):
        global step_true
        step_true = 0
        global cip
        cip = 1
        bot.send_message(message.chat.id, "Включен режим шифрования, напишите текст")


    @bot.message_handler(commands=["Дэшифровать"])
    def disciphering_mode(message):
        bot.send_message(message.chat.id, "Включен режим дэшифрования, напишите текст")
        global step_true
        step_true = 0
        global cip
        cip = 0

    @bot.message_handler(commands=["Шаг"])
    def set_step(message):
        bot.send_message(message.chat.id, "Задайте шаг сдвига")
        global step_true
        step_true = 1
        global cip
        cip = 2

    @bot.message_handler(content_types=["text"])
    def ciphering(message):
        global step_true
        if step_true == 1:
            if message.text.isnumeric():
                global step
                step = int(message.text)
                step_true = 0
            else:
                bot.send_message(message.chat.id, "Ошибка! Повторите попытку")


        if cip == 1:
            bot.send_message(message.chat.id, Cipher(step, message.text))
        elif cip == 0:
            bot.send_message(message.chat.id, disCipher(step, message.text))
        else:
            bot.send_message(message.chat.id, "Включите какой нибудь режим")



    bot.polling()
if __name__ == '__main__':
    telegram_bot(token)