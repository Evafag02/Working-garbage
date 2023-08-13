import telebot
from telebot import types

token = '5940236147:AAESEqt5_BAfg31etfXmSs1MeOtQ6V33cQQ'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(msg):  # Название функции не играет никакой роли

    if(msg.text.lower() == 'hello' or msg.text.lower() == 'hi'):
        keyboard = types.InlineKeyboardMarkup()
        key_narxoz = types.InlineKeyboardButton(
            text='Narxoz', url='https://www.narxoz.kz')
        key_itmo = types.InlineKeyboardButton(
            text='ITMO', url='https://www.ifmo.ru')
        key_google = types.InlineKeyboardButton(
            text='Google', url='https://www.google.com')
        keyboard.add(key_narxoz, key_itmo)
        keyboard.add(key_google)
        bot.send_message(
            msg.chat.id, text='Hello, '+msg.from_user.first_name+'! Choose the site below', reply_markup=keyboard)

    elif (msg.text.lower() == 'привет' or msg.text.lower() == 'здравствуй' or msg.text.lower() == 'здравствуйте'):
        keyboard = types.InlineKeyboardMarkup()
        key_narxoz = types.InlineKeyboardButton(
            text='Narxoz', url='https://www.narxoz.kz')
        key_itmo = types.InlineKeyboardButton(
            text='ITMO', url='https://www.ifmo.ru')
        key_google = types.InlineKeyboardButton(
            text='Google', url='https://www.google.com')
        keyboard.add(key_narxoz, key_itmo)
        keyboard.add(key_google)
        bot.send_message(
            msg.chat.id, text='Привет, '+msg.from_user.first_name+'! Выбери сайт ниже', reply_markup=keyboard)
    elif(msg.text.lower() == 'данные'):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(
            msg.chat.id,
            text='Привет, ' + msg.from_user.first_name +
                              '! Отправь мне свой номер телефона',
                              reply_markup=keyboard)
    else:
        bot.send_message(msg.chat.id, 'Эхо: '+msg.text)


# if _name_ == '_main_':
#      bot.infinity_polling()

bot.polling()
