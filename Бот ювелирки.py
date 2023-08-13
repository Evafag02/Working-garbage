import telebot, time
from telebot import types  # для указание типов

bot = telebot.TeleBot('6077138414:AAFMMA0Lt2YHWp7Cwq2supUauxNgNgLdxOM')

print('bot online', time.strftime('%X'))

@bot.message_handler(commands=['start'])  # создаем команду
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Оформить заказ 📝")
    btn2 = types.KeyboardButton("Отмена ❌")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, '''Я бот магазина bijoupvl
Здесь вы можете посмотреть наши украшения'''.format(message.from_user), reply_markup=markup)

imagee = ['photo_5334535491611117987_y.jpg', 'photo_5334535491611117988_y.jpg','photo_5334535491611117997_x.jpg', 'photo_5334535491611118013_x.jpg', 'photo_5334535491611118014_x.jpg',
        'photo_5334535491611118015_x.jpg', 'photo_5337307751266764256_x.jpg']

@bot.message_handler(content_types=['text'])  # создаем команду
def start_message(message):
    if message.text == 'Оформить заказ 📝':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        btn5 = types.KeyboardButton("5")
        btn6 = types.KeyboardButton("6")
        btn7 = types.KeyboardButton("7")
        btn8 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, 'В наличии: ',reply_markup=markup)
        bot.send_media_group(message.chat.id,[telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in imagee])

    if message.text == "1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[0], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 550',reply_markup=markup)

    if message.text == "2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[1], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 350',reply_markup=markup)

    if message.text == "3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[2], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 1000',reply_markup=markup)

    if message.text == "4":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[3], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 650',reply_markup=markup)

    if message.text == "5":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[4], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 400',reply_markup=markup)

    if message.text == "6":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[5], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 450',reply_markup=markup)

    if message.text == "7":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn3)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open(imagee[6], 'rb'))])
        bot.send_message(message.chat.id, text='стоимость: 500', reply_markup=markup)

    elif message.text == "Оплатить 💵":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Подтвердить ✅")
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Укажите ваш адрес, имя и номер телефона, это нужно для связи с вами'
                         .format(message.from_user), reply_markup=markup)

    elif message.text == "Подтвердить ✅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Спасибо за покупку, будем ждать вас снова"
                         .format(message.from_user), reply_markup=markup)

    elif message.text == "Вернуться назад 🔁":
        start(message)

    elif message.text == "Отмена ❌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Бот остановлен", reply_markup=markup)

bot.polling(none_stop=True, interval=0)
