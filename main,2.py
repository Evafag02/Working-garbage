import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot('5940236147:AAESEqt5_BAfg31etfXmSs1MeOtQ6V33cQQ')

ingredients = ['Оливки', 'Помидоры', 'Сыр', 'Ветчина', 'Пепперони из говядины', 'Ананас', 'Охотничьи колбаски',
               'Шампиньоны', 'Сырные бортики🧀']
order = ['Ваш заказ это:']
price = 0
fio = ""


@bot.message_handler(commands=['start'])  # создаем команду
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Оформить заказ 📝")
    btn2 = types.KeyboardButton("Отмена ❌")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, '''Я Piiizzzaaa_bot🍕! 
Бот сети пиццерий в Алмате под названием 'BestPizza🍕' 
Помогу тебе легко сделать заказ или создать самую 
вкусную пиццу по твоим предпочтениям 😋'''.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    global price, order, fio

    if message.text == "Оформить заказ 📝" or message.text == "Дополнить заказ 📝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Маргарита")
        btn2 = types.KeyboardButton("Овощи и грибы")
        btn3 = types.KeyboardButton("Пепперони")
        btn4 = types.KeyboardButton("Супер сырная")
        btn5 = types.KeyboardButton("4 сезона")
        btn6 = types.KeyboardButton("Мясной микс")
        btn7 = types.KeyboardButton("Гавайская")
        btn8 = types.KeyboardButton("Составьте пиццу сами")
        btn9 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, '''⚠️ Все пиццы из нашего меню Халяль
Выберите пиццу из нашего меню или составьте свою уникальную пиццу'''.format(message.from_user), reply_markup=markup)

    elif message.text == "Отмена ❌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Бот остановлен", reply_markup=markup)

    elif message.text == "Маргарита":
        price += 2100
        order.append(" ")
        order.append("Маргарита🍕")
        bot.send_photo(message.chat.id, photo=open('photo_5195192948503987670_y.jpg', 'rb'), caption='''Маргарита
Большая порция моцареллы, томаты, базилик, томатный соус
2100 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)



    elif message.text == "Овощи и грибы":
        price += 2200
        order.append(" ")
        order.append("Овощи и грибы🍕")
        bot.send_photo(message.chat.id, photo=open('photo_5195192948503987681_x.jpg', 'rb'), caption='''Овощи и грибы
Шампиньоны, томаты, сладкий перец, красный лук, брынза, моцарелла, томатный соус
2200 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)


    elif message.text == "Пепперони":
        price += 2500
        order.append(" ")
        order.append("Пепперони🍕")
        bot.send_photo(message.chat.id, photo=open('photo_5195192948503987684_y.jpg', 'rb'), caption='''Пепперони
Пепперони, увеличенная порция моцареллы, томатный соус
2500 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)



    elif message.text == "Супер сырная":
        price += 2500
        order.append(" ")
        order.append("Супер сырная🍕")
        bot.send_photo(message.chat.id, photo=open('photo_5195192948503987689_y.jpg', 'rb'), caption='''Супер сырная
Моцарелла, пармезан, чедер и сыр фонтина
2500 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)



    elif message.text == "4 сезона":
        price += 2700
        order.append(" ")
        order.append("4 сезона🍕")
        bot.send_photo(message.chat.id, photo=open('photo_5195192948503987695_x.jpg', 'rb'), caption='''4 сезона
Моцарелла, ветчина из цыплёнка, пепперони из говядины, кубики брынзы, томаты, шампиньоны, сырный соус
2700 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)



    elif message.text == "Мясной микс":
        price += 2600
        order.append(" ")
        order.append("Мясной микс🍕")
        bot.send_photo(message.chat.id, photo=open('photo_5195192948503987706_x.jpg', 'rb'), caption='''Мясной микс
Цыплёнок, ветчина из индейки, говяжий фарш, томатный соус, моцарелла
2600 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)



    elif message.text == "Гавайская":
        price += 2500
        order.append(" ")
        order.append("Гавайская🍕")

        bot.send_photo(message.chat.id, photo=open('photo_5197472579705751236_x.jpg', 'rb'), caption='''Гавайская
Ветчина из индейки, томатный соус, моцарелла, ананас, базелик, помидор
2500 тг''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)



    elif message.text == "Составьте пиццу сам":
        price += 3000
        order.append(" ")
        order.append("Уникальная пицца🍕")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оливки")
        btn2 = types.KeyboardButton("Помидоры")
        btn3 = types.KeyboardButton("Сыр")
        btn4 = types.KeyboardButton("Ветчина")
        btn5 = types.KeyboardButton("Пепперони из говядины")
        btn6 = types.KeyboardButton("Ананасы")
        btn7 = types.KeyboardButton("Охотничьи колбаски")
        btn8 = types.KeyboardButton("Шампиньоны")
        btn9 = types.KeyboardButton("Сделать заказ")
        btn10 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_photo(message.chat.id, photo=open('photo_5197556950043311599_y.jpg', 'rb'), caption='''
Составь пиццу сами (3000 тг):
1) Оливки
2) Помидоры
3) Сыр
4) Ветчина
5) Пепперони из говядины
6) Ананасы
7) Охотничьи колбаски
8) Шампиньоны
9) Сделать заказ
10) Вернуться назад'''.format(message.from_user), reply_markup=markup)

    elif message.text == "Оливки":
        order.append(ingredients[0])

    elif message.text == "Помидоры":
        order.append(ingredients[1])

    elif message.text == "Сыр":
        order.append(ingredients[2])

    elif message.text == "Ветчина":
        order.append(ingredients[3])

    elif message.text == "Пепперони из говядины":
        order.append(ingredients[4])

    elif message.text == "Ананасы":
        order.append(ingredients[5])

    elif message.text == "Охотничьи колбаски":
        order.append(ingredients[6])

    elif message.text == "Шампиньоны":
        order.append(ingredients[7])

    elif message.text == "Сделать заказ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да, добавить ✅")
        btn2 = types.KeyboardButton("Нет, не добавлять ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Добавить сырные бортики 🧀 (300тг)?".format(message.from_user),
                         reply_markup=markup)


    elif message.text == "Да, добавить ✅":
        price += 300
        order.append(ingredients[8])
        bot.send_message(message.chat.id, '\n'.join(order))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да это то что я выбрал(а)✅")
        btn2 = types.KeyboardButton("Нет, это не то ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, f'Стоимость: {price}')
        bot.send_message(message.chat.id, text="Это то что вы выбрали?".format(message.from_user),
                         reply_markup=markup)

    elif message.text == "Нет, не добавлять ❌":
        bot.send_message(message.chat.id, '\n'.join(order))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да это то что я выбрал(а)✅")
        btn2 = types.KeyboardButton("Нет, это не то ❌")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, f'Стоимость: {price}')
        bot.send_message(message.chat.id, text="Это то что вы выбрали?".format(message.from_user), reply_markup=markup)

    elif message.text == "Да это то что я выбрал(а)✅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Оплатить 💵")
        btn2 = types.KeyboardButton("Дополнить заказ 📝")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Оплатить? или желаете еще что-то взять?".format(message.from_user),
                         reply_markup=markup)


    elif message.text == "Оплатить 💵":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Доставка 💵")
        btn2 = types.KeyboardButton("Самовывоз 📝")
        btn3 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text='''Заказать доставку или самовывоз?
АКЦИЯ - за самовывоз, даем в подарок 1л Coca-Cola
Доставка от 5000тг БЕСПЛАТНАЯ
Внутри Алматы 1000тг'''.format(message.from_user), reply_markup=markup)

    elif message.text == "Самовывоз 📝":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Ваш заказ будет готов через 30 минут, мы находимся по адресу 'Жандосова 15'"
                         .format(message.from_user), reply_markup=markup)

    elif message.text == "Доставка 💵":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Подтвердить ✅")
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Укажите ваш адрес, имя и номер телефона, это нужно для связи с вами'
                         .format(message.from_user), reply_markup=markup)

    elif message.text == "Подтвердить ✅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться назад 🔁")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Хорошо, курьер прибудет в течении 60-90 минут"
                         .format(message.from_user), reply_markup=markup)


    elif message.text == "Вернуться назад 🔁" or message.text == "Нет, это не то ❌":
        order = ['Ваш заказ это:']
        price = 0
        start(message)


bot.polling(none_stop=True, interval=0)
