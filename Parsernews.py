import telebot
import requests
import time

from bs4 import BeautifulSoup

token = "6383545026:AAFsnGx11cHu3c648dmblrGvtA0pTQkaqtE"  # Your token
channel_id = "@Pythonews_kz"  # Your channel login in telegram
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == "/start":
        back_post_check = None
        while True:
            post_text = parser(back_post_check)
            back_post_check = post_text[1]
            if post_text[0] != None:
                bot.send_message(channel_id, post_text[0])
                time.sleep(1)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start")


def parser(back_post_check):
    URL = "https://kp.ua/archive/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    post = soup.find("div", class_="materials archive archive-bl")
    post_check = post
    if post_check != back_post_check:
        title = post.find("a", class_="materials__title").text.strip()
        description = post.find("span", class_="materials__text").text.strip()
        ending_url = post.find("a", class_="materials__title", href=True)["href"].strip()
        url = 'https://kp.ua' + ending_url
        print(title, description, url)
        return f"{title}\n\n{description}\n\n{url}", post_check
    else:
        return None, post_check


bot.polling()