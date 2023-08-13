import telebot
from telebot import types


from telebot.types import KeyboardButton

bot=telebot.TeleBot('5786214677:AAEPJ9fsnAfhhIuT_1XveiAR0kzqLzdODBA')

@bot.message_handler(commands=['start','help'])
def send_welcome(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    itembtn1=types,KeyboardButton('Помощь')
    itembtn2=types,KeyboardButton('Связь с нами')
    itembtn3=types,KeyboardButton('Перевод слов')
    markup.add(itembtn1,itembtn2,itembtn3)
    mesg = bot.send_message(message.chat.id,'Здравствуйте!Рад вас видеть.Я бот-переводчик и помогу Вам перевести русские слова на казахский.Выберите пожалуйста нужный вам раздел.',reply_markup=markup)
    bot.register_next_step_handler(mesg, process_words)
def process_words(message):
    bot.send_message(message.chat.id,'Напишите мне')
    try:
        if message.text== 'Избранные слова':
            mark_words(message)
        elif message.text =='Учить свои слова':
            mark_words(message)
        elif message.text =='Связь с нами':
            call_me(message)

    except Exception as e:
        bot.reply_to(message, 'ooops!')


def mark_words(message):
    Selected_words=telebot.types.InlineKeyboardButton(text='Избранные слова', callback_data='command1')
    Learn_own_words=telebot.types.InlineKeyboardButton(text='Учить свои слова',callback_data='command2')
    Contact_us =telebot.types.InlineKeyboardButton(text='Связь с вами',callback_data='command3')
    Unknown_words=telebot.types.InlineKeyboardButton(text='Неизвестные слова',callback_data='command4')

    markup_inline=telebot.types.ReplyKeyboardMarkup()
    markup_inline.add(Selected_words)
    markup_inline.add(Learn_own_words)
    markup_inline.add(Contact_us)
    markup_inline.add(Unknown_words)

    bot.send_message(message.chat.id,"Отлично,теперь выберите слова",reply_markup=markup_inline)

def help(message, markup_inline=None):
    bot.send_message(message.chat.id,'Чтобы начать нажмите на start или наберите',reply_markup=markup_inline)

def call_me(message):
    bot.send_message(message.chat.id,'Наши контакты:WhatsApp:+7 (707) 801 69 00')
@bot.callback_query_handler(func=lambda call:True)
def answer_to_callback(call):
    if call.data =='command1':
        bot.send_message(chat_id=call.message.chat.id,text='Теперь выберите интересующую вас слово.')
        bot.send_message(chat_id=call.message.chat.id, text='Кәмелет- для получение больше информации об этом слове нажмите /Кәмелет')
        bot.send_message(chat_id=call.message.chat.id, text='Әтір - для получение больше информации об этом слове нажмите /Әтір')
        bot.send_message(chat_id=call.message.chat.id, text='Қылтима - для получение больше информации об этом слове,Қылтима/')
        bot.send_message(chat_id=call.message.chat.id, text='Төраға - для получение больше информации об этом слове,Төраға/')
        bot.send_message(chat_id=call.message.chat.id,text='Белдемше-для получение больше информации об этом слове,Белдемше/')

@bot.message_handler(commands=["Кәмелет"])
def start_message(message):
        Mean=telebot.types.InlineKeyboardButton(text='Узнать значение',callback_data='Mean')

        markup_inline=telebot.types.ReplyKeyboardMarkup()
        markup_inline.add(Mean)
        bot.send_photo(message.chat.it,photo='https://calendarbox.ru/wp-content/uploads/2020/06/a4-raspechatatka-zyfry-18.png')
        bot.send_message(message.chat.id,"Говорят, что те, кому 18 лет, достигли совершеннолетия.")\

        @bot.message_handler(commands=["Әтір"])

        def start_message(message):
          Mean = telebot.types.InlineKeyboardButton(text='Узнать значение', callback_data='Mean')
        markup_inline = telebot.types.ReplyKeyboardMarkup()
        markup_inline.add(Mean)
        bot.send_photo(message.chat.it, photo='https://cdn.nur.kz/images/1120/30670ad4619de47d.jpeg')
        bot.send_message(message.chat.id, "Ароматическое жидкое вещество,либо духи,парфюм")
@bot.message_handler(commands=["Қылтима"])
def start_message(message):
        Mean = telebot.types.InlineKeyboardButton(text='Узнать значение',callback_data='Mean')

        markup_inline = telebot.types.ReplyKeyboardMarkup()
        markup_inline.add(Mean)
        bot.send_photo(message.chat.it, photo='https://www.stroyportal.ru/media/cache/companies/38763/products/684522446/200fa16b-8300-4a85-9718-ab968eda71cd_small_mobile_image.jpg')
        bot.send_message(message.chat.id, "Балкон")
@bot.message_handler(commands=["Қылтима"])
def start_message(message):
        Mean = telebot.types.InlineKeyboardButton(text='Узнать значение', callback_data='Mean')

        markup_inline = telebot.types.ReplyKeyboardMarkup()
        markup_inline.add(Mean)
        bot.send_photo(message.chat.it, photo='https://www.stroyportal.ru/media/cache/companies/38763/products/684522446/200fa16b-8300-4a85-9718-ab968eda71cd_small_mobile_image.jpg')
        bot.send_message(message.chat.id, "Балкон")
@bot.message_handler(commands=["Төреаға"])
def start_message(message):
        Mean = telebot.types.InlineKeyboardButton(text='Узнать значение', callback_data='Mean')

        markup_inline = telebot.types.ReplyKeyboardMarkup()
        markup_inline.add(Mean)
        bot.send_photo(message.chat.it, photo='https://fresh.acit-c.ru/templates/yootheme/cache/manager-7c762b12.jpeg')
        bot.send_message(message.chat.id, "Руководитель")
@bot.message_handler(commands=["Белдемше"])
def start_message(message):
        Mean = telebot.types.InlineKeyboardButton(text='Узнать значение', callback_data='Mean')

        markup_inline = telebot.types.ReplyKeyboardMarkup()
        markup_inline.add(Mean)
        bot.send_photo(message.chat.it, photo='https://static.baza.farpost.ru/v/1497318864093_bulletin')
        bot.send_photo(message.chat.id, "Юбка")

bot.polling()