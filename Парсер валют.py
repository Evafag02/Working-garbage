import telebot
import requests

from bs4 import BeautifulSoup

token = "6383545026:AAE_vnWlM3NXQXcI0R_Fy97IlVt3CeSZcKs"  # ыВаш токен
channel_id = "@Pythonews_kz"  # Ваш логин канала
bot = telebot.TeleBot(token)

def parser():
    URL = "https://www.nur.kz/nurfin/exchange-rates-nbrk/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('div', class_='tableBody-0-2-19')
    dollar = table.find('div', class_='tableColumn-0-2-21 textRight-0-2-12').text.strip()
    dollar_currency = 'Доллар - ' + dollar
    print(dollar_currency)

parser()