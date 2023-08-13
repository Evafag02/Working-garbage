import telebot
import requests

gismeteo_token = "56b30cb255.3443075"
token_bot = "6383545026:AAE_vnWlM3NXQXcI0R_Fy97IlVt3CeSZcKs"  # Ваш токен
channel_id = "@Pythonews_kz"  # Ваш логин канала
bot = telebot.TeleBot(token_bot)



@bot.message_handler(content_types=['text'])
def commands(message):
    print(X)
bot.polling()