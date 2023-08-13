import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot('6006000440:AAHMOBJXR-LcI4S5p9R918GtgyN7WOTjb4U')

print('bot online')

@bot.message_handler(commands=['start'])  # создаем команду
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Русский язык")
    btn2 = types.KeyboardButton("Қазақ тілі")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '''Қандай тілде ыңғайлы сізге?
(На каком языке вам удобнее?)'''.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])  # создаем команду
def start_message(message):
    if message.text == 'Русский язык':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Макияж") # РУССКИЙ
        btn2 = types.KeyboardButton("Прическа") # РУССКИЙ
        btn3 = types.KeyboardButton("Маникюр") # РУССКИЙ
        btn4 = types.KeyboardButton("Педикюр") # РУССКИЙ
        btn8 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn8)
        bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
        bot.send_message(message.chat.id, '''Какая помощь/услуга вам нужна?'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Қазақ тілі':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Мaкияж")  # КАЗ (англ а)
        btn2 = types.KeyboardButton("Прическa") # КАЗ (англ а)
        btn3 = types.KeyboardButton("Мaникюр") # КАЗ (англ а)
        btn4 = types.KeyboardButton("Пeдикюр") # КАЗ (англ e)
        btn9 = types.KeyboardButton("артқа қайту 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn9)
        bot.send_message(message.chat.id, 'Сәлеметсіз бе, ' + message.from_user.first_name)
        bot.send_message(message.chat.id, '''Сізге қандай көмек қажет?'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Мaкияж':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("9:30")
        btn1 = types.KeyboardButton("11:00")
        btn2 = types.KeyboardButton("13:00")
        btn3 = types.KeyboardButton("15:15")
        btn4 = types.KeyboardButton("17:30")
        btn5 = types.KeyboardButton("19:00")
        btn9 = types.KeyboardButton("артқа қайту 🔁")
        markup.add(btn0, btn1, btn2, btn3, btn4, btn5, btn9)
        bot.send_message(message.chat.id, '''Бос уақыттар:'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Прическa':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("9:30")
        btn2 = types.KeyboardButton("12:00")
        btn3 = types.KeyboardButton("13:15")
        btn4 = types.KeyboardButton("14:30")
        btn5 = types.KeyboardButton("16:45")
        btn6 = types.KeyboardButton("18:30")
        btn9 = types.KeyboardButton("артқа қайту 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn9)
        bot.send_message(message.chat.id, '''Бос уақыттар:'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Мaникюр':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10:00")
        btn2 = types.KeyboardButton("11:30")
        btn3 = types.KeyboardButton("12:45")
        btn4 = types.KeyboardButton("14:30")
        btn5 = types.KeyboardButton("16:00")
        btn6 = types.KeyboardButton("17:30")
        btn9 = types.KeyboardButton("артқа қайту 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn9)
        bot.send_message(message.chat.id, '''Бос уақыттар:'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Пeдикюр':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10:00")
        btn2 = types.KeyboardButton("13:00")
        btn3 = types.KeyboardButton("14:45")
        btn4 = types.KeyboardButton("16:30")
        btn5 = types.KeyboardButton("17:00")
        btn9 = types.KeyboardButton("артқа қайту 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn9)
        bot.send_message(message.chat.id, '''Бос уақыттар:'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Макияж':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("9:30")
        btn1 = types.KeyboardButton("11:00")
        btn2 = types.KeyboardButton("13:00")
        btn3 = types.KeyboardButton("15:15")
        btn4 = types.KeyboardButton("17:30")
        btn5 = types.KeyboardButton("19:00")
        btn8 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn0, btn1, btn2, btn3, btn4, btn5, btn8)
        bot.send_message(message.chat.id, '''Свободные окна:'''.format(message.from_user),
                         reply_markup=markup)



    elif message.text == 'Прическа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("9:30")
        btn2 = types.KeyboardButton("12:00")
        btn3 = types.KeyboardButton("13:15")
        btn4 = types.KeyboardButton("14:30")
        btn5 = types.KeyboardButton("16:45")
        btn6 = types.KeyboardButton("18:30")
        btn8 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8)
        bot.send_message(message.chat.id, '''Свободные окна:'''.format(message.from_user),
                         reply_markup=markup)

    elif message.text == 'Маникюр':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10:00")
        btn2 = types.KeyboardButton("11:30")
        btn3 = types.KeyboardButton("12:45")
        btn4 = types.KeyboardButton("14:30")
        btn5 = types.KeyboardButton("16:00")
        btn6 = types.KeyboardButton("17:30")
        btn8 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn8)
        bot.send_message(message.chat.id, '''Свободные окна:'''.format(message.from_user),
                         reply_markup=markup)


    elif message.text == 'Педикюр':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10:00")
        btn2 = types.KeyboardButton("13:00")
        btn3 = types.KeyboardButton("14:45")
        btn4 = types.KeyboardButton("16:30")
        btn5 = types.KeyboardButton("17:00")
        btn8 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn8)
        bot.send_message(message.chat.id, '''Свободные окна:'''.format(message.from_user),
                         reply_markup=markup)


    elif len(message.text) == 5:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сулушаш")
        btn2 = types.KeyboardButton("Арыстан")
        btn3 = types.KeyboardButton("Айгерим")
        btn4 = types.KeyboardButton("Эльмира")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text='''Сізбен байланысу үшін, атыңызды және телефон нөміріңізді қалдырыңыз:
(Выберите мастера):'''.format(message.from_user), reply_markup=markup)

    elif len(message.text) == 7:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сохранить данные ✅")
        btn2 = types.KeyboardButton('деректерді сақтау✅')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='''Сізбен байланысу үшін, атыңызды және телефон нөміріңізді қалдырыңыз:
(Оставьте ваше имя, и номер телефона, чтобы мы смогли с вами связаться):'''.format(message.from_user), reply_markup=markup)


    elif message.text == "Сохранить данные ✅" or message.text == 'деректерді сақтау✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться назад 🔁")
        btn2 = types.KeyboardButton("артқа қайту 🔁")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='''Біз сізді күтеміз, рахмет, сау болыңыз!
(Будем вас ждать, спасибо досвидания!):'''.format(message.from_user), reply_markup=markup)


    elif message.text == "Вернуться назад 🔁" or message.text == "артқа қайту 🔁":
        start(message)


bot.polling(none_stop=True, interval=0)
