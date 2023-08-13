import telebot


bot = telebot.TeleBot('5940236147:AAESEqt5_BAfg31etfXmSs1MeOtQ6V33cQQ')

@bot.message_handler(commands=['start'])  # создаем команду
def start(message):
    bot.send_message(message.chat.id, f'''Hello {message.from_user.first_name}
I am a bot that will help you calculate your GPA
Enter a score (0-100) in % and we'll tell you your GPA''')


@bot.message_handler(content_types=['text'])
def func(message):
    if 100 >= int(r) >= 0:
        if 24 >= int(r) >= 0:
            bot.send_message(message.chat.id, "Your GPA is - F (0)")
            bot.send_message(message.chat.id, "This is unsatisfactorily")
        elif 49 >= int(r) >= 25:
            bot.send_message(message.chat.id, "Your GPA is - FX (0,5)")
            bot.send_message(message.chat.id, "This is unsatisfactorily")
        elif 54 >= int(r) >= 50:
            bot.send_message(message.chat.id, "Your GPA is - D- (1)")
            bot.send_message(message.chat.id, "This is unsatisfactorily")
        elif 59 >= int(r) >= 55:
            bot.send_message(message.chat.id, "Your GPA is - D+ (1,33)")
            bot.send_message(message.chat.id, "This is unsatisfactorily")
        elif 64 >= int(r) >= 60:
            bot.send_message(message.chat.id, "Your GPA is - C- (1,67)")
            bot.send_message(message.chat.id, "This is unsatisfactorily")
        elif 69 >= int(r) >= 65:
            bot.send_message(message.chat.id, "Your GPA is - C (2)")
            bot.send_message(message.chat.id, "This is satisfactory")
        elif 74 >= int(r) >= 70:
            bot.send_message(message.chat.id, "Your GPA is- C+ (2,33)")
            bot.send_message(message.chat.id, "This is satisfactory")
        elif 79 >= int(r) >= 75:
            bot.send_message(message.chat.id, "Your GPA is - B- (2,67)")
            bot.send_message(message.chat.id, "This is satisfactory")
        elif 84 >= int(r) >= 80:
            bot.send_message(message.chat.id, "Your GPA is - B (3)")
            bot.send_message(message.chat.id, "This is satisfactory")
        elif 89 >= int(r) >= 85:
            bot.send_message(message.chat.id, "Your GPA is - B+ (3,33)")
            bot.send_message(message.chat.id, "This is good")
        elif 94 >= int(message.text) >= 90:
            bot.send_message(message.chat.id, "Your GPA is - A- (3,67)")
            bot.send_message(message.chat.id, "Good")
        elif 100 >= int(message.text) >= 95:
            bot.send_message(message.chat.id, "Your GPA is - A (4)")
            bot.send_message(message.chat.id, "Great")
    else:
        bot.send_message(message.chat.id, "invalid value, enter a number from 0 to 100")


bot.polling(none_stop=True, interval=0)
