"""Вступ до HTTP, створення HTTP-запитів"""

"""Task 1
Robots.txt
Download and save to file robots.txt from wikipedia,
 twitter websites etc. """

import requests
from bs4 import BeautifulSoup


class Robots:
    def __init__(self):
        self.save_to_file()

    def get_data(self):
        r = requests.get(
            "https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B1%D0%BE%D1%82_(%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)")
        data = r.text
        return data

    def parse_data(self):
        soup = BeautifulSoup(self.get_data(), "xml")
        w_text = soup.find("div", class_="mw-parser-output")
        return w_text.text

    def save_to_file(self):
        with open("robots.txt", "w", encoding="utf-8") as file:
            file.write(self.parse_data())


rob = Robots()

"""Task 2
Load data
Download all comments from a subreddit of your choice using URL:
https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in 
chronological order in JSON and dump it to a file."""

import requests
import datetime
import json


class LoadComments:
    def __init__(self):
        self.api = "https://api.pushshift.io/reddit/comment/search/"
        self.data = self.get_data()

    def get_data(self):
        r = requests.get(self.api)
        return r.json()

    def data_parse(self):
        new_data = {}
        for i in self.data["data"]:
            author = i["author"]
            msg = i["body"]
            time = datetime.datetime.utcfromtimestamp(i["created_utc"]).strftime("%d-%m-%Y, %H:%M:%S")
            id_ = i["id"]
            data = {id_: {"Author": author,
                          "Msg": msg,
                          "Time": time}}
            new_data.update(data)
        return new_data

    def save_to_file(self):
        with open("data_pushshift.json", "w", encoding="utf-8") as file:
            json.dump(self.data_parse(), file, ensure_ascii=False, indent=4)


comments = LoadComments()
comments.save_to_file()

"""Task 3
The Weather app
Write a console application which takes as an input 
a city name and returns current weather in the format of your choice. 
For the current task, you can choose any weather API 
or website or use https://openweathermap.org """

import datetime
import requests
from token_weather_bot import token
from weather_api_key import api_key
from telebot import types
import telebot
import random
import pytz
import os


class Weather:
    def __init__(self, message):
        self.__api_key = api_key
        self.data = self.get_data(message)
        self.image = None

    def get_data(self, msg):
        r = requests.get(f"http://api.openweathermap.org/data/2.5/find?q={msg}&appid={self.__api_key}&lang=ru&units=metric")
        data = r.json()
        return data

    @property
    def weather_data(self):
        try:
            return self.show_weather()
        except:
            return self.wrong_input()

    def show_weather(self):
        feels_like = self.data["list"][0]["main"]["feels_like"]
        name = self.data["list"][0]["name"]
        temp = self.data["list"][0]["main"]["temp"]
        description = self.data["list"][0]["weather"][0]["description"].capitalize()
        time_ = datetime.datetime.now(tz=pytz.timezone('Etc/GMT-2')).strftime("%Y-%m-%d %H:%M")
        ans = f"***{time_}*** \nВ городе {name} температура {temp}С°, ощущается как {feels_like}С°,\n{description}"
        self.weather_image()
        return ans

    def wrong_input(self):
        list_of_answers = ["Нет такого города. Иль чет типа того. \nПопробуй заново",
                           "Эээ... Ну, тут, как бы, нужно указать название города.\n Давай еще раз",
                           "Ну и что ты ввел?! Кто мог так назвать город?! \nЛадно, давай еще раз. Только смотри, что пишешь",
                           "Ты серьезно?! Писать разучился?! \nНАПИШИ НАЗВАНИЕ ГОРОДА",
                           "Три, два, раз - с детства с рифмой я дружу. \nА ты не отвлекайся. Давай заново"]
        list_of_imgs = ["try_again.png", "try_again1.jpg", "try_again2.png", "try_again3.jpg", "try_again4.jpg"]
        image = random.choice(list_of_imgs)
        img = open(image, "rb")
        self.image = img.read()
        img.close()
        answer = random.choice(list_of_answers)
        return answer

    def weather_image(self):
        weather_images = {
            "Clouds": "cloudy_.jpg",
            "Snow": "snowy.jpg",
            "Rain": "rainy_day.jpg",
            "Thunderstorm": "thunder.jpg",
            "Clear": "sunny-day.jpg",
            "Fog": "Fog.jpg",
            "Mist": "Fog.jpg"
        }
        if self.data["list"][0]["weather"][0]["main"] in weather_images:
            img = open(weather_images[self.data["list"][0]["weather"][0]["main"]], "rb")
            self.image = img.read()
            img.close()


class ExchangeRate:
    def __init__(self, currencies: list):
        self.__data = self.data_parse()
        self.currencies = currencies

    def data_parse(self):
        currency = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        data = currency.json()
        return data

    @property
    def exchange_rate(self):
        try:
            currencies_list = []
            for i in self.__data:
                if i["cc"] in self.currencies:
                    idx = self.__data.index(i)
                    text = self.__data[idx]["txt"]
                    rate = self.__data[idx]["rate"]
                    date = self.__data[idx]["exchangedate"]
                    curr_rate = f"{text} / UAH: {rate}, {date}"
                    currencies_list.append(curr_rate)
            what_to_send = "\n".join(currencies_list) + "\n" + 3 * "\U0001F601"
            return what_to_send
        except:
            return "Что-то пошло не так"


bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_msg(message):
    bot.send_message(message.chat.id, "Здарова. Город напиши, а там поговорим...")


@bot.message_handler(content_types=["text"])
def send_data_to_bot(message):
    msg = message.text
    weather = Weather(msg)
    bot.send_message(message.chat.id, weather.weather_data)
    bot.send_photo(message.chat.id, weather.image)

    inline_markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Да", callback_data="dada")
    button2 = types.InlineKeyboardButton("Нет", callback_data="nene")
    inline_markup.add(button1, button2)
    bot.send_message(message.chat.id, "Курсы валют?", reply_markup=inline_markup)

    save_logs1(message)


@bot.callback_query_handler(func=lambda call: call.data in ["dada", "nene"])
def show_currencies(call):
    fun_sticker = ["CAACAgQAAxkBAAIRNGIWeBlej1fy1oYSuvLsNR-fw_LeAAMCAALictkAATtHXkmnOXtwIwQ",
                   "CAACAgQAAxkBAAIRNmIWeCkD9aKSpKPV16_sLFTdbWjIAAL-AQAC4nLZAAF1sqOo2X-g4yME",
                   "CAACAgQAAxkBAAIROGIWeEPadfXsmB-VIVPC4tEFsWgPAAIMAgAC4nLZAAFcfq4ZGAABhX0jBA",
                   "CAACAgQAAxkBAAIROmIWeFBJQ6MH96VtuDcsHsgZGXJwAAIgAgAC4nLZAAGQrNHOjgzELCME",
                   "CAACAgIAAxkBAAIRQGIWeNvaI9kqUrUrLDjMTFAzes3hAAIVFwACn1WYS4Rq172hwZEtIwQ",
                   "CAACAgIAAxkBAAIRQmIWeQEnwh6XxtHXj24MJSMj_C66AAL5FQAC-dypS5_OYgwbqiDIIwQ"]
    mad_sticker = ["CAACAgQAAxkBAAIRAAFiFnY8emZnpdY_ygTaVrL8spCOlgACBAIAAuJy2QABw5aUAS4Z8j4jBA",
                   "CAACAgQAAxkBAAIRAmIWdmHBeAnubhCQ5QnESHFtxSJlAAIYAgAC4nLZAAHh8-bonAYRCiME",
                   "CAACAgQAAxkBAAIRBGIWdnOpWn8qDZguWoxq3zkJWh-1AAICAgAC4nLZAAG2m-bIlzNzuCME",
                   "CAACAgQAAxkBAAIRCGIWdpJJqf0IfGNxfD4DguhG-0XpAAIaAgAC4nLZAAF4R6ue7bQqcyME",
                   "CAACAgQAAxkBAAIRCmIWdp6sGnWWdLHd5uyeToobHGX4AAI2AgAC4nLZAAFCf6_FmA-toCME",
                   "CAACAgIAAxkBAAIRHGIWdyQ_DG8YTsACBfrToAo_I8NzAAItCQACLw_wBjLtpfV8EWOXIwQ",
                   "CAACAgIAAxkBAAIRHmIWd0EOPjFNIDcEbQABn6nRgRwIsgACMwkAAi8P8AbGkUGP5_C5_yME",
                   "CAACAgIAAxkBAAIRImIWd3D5ZBt22RDl88EQPTC56uWwAAKIAQACjkQRAvtWR7xNt8BzIwQ",
                   "CAACAgIAAxkBAAIRLGIWd53HLq8v03cWtrVnWom1UCmiAAKRAQACjkQRAkPbAXQpF792IwQ",
                   "CAACAgIAAxkBAAIRMGIWd7q9euTBJSVcbNfvfy-ZZdUDAALABAACIG07AAFVsfrgNlI4AiME"]
    send_fun_sticker = random.choice(fun_sticker)
    send_mad_sticker = random.choice(mad_sticker)
    if call.data == "dada":
        currency = ExchangeRate(["USD", "EUR", "PLN"])
        bot.send_sticker(call.message.chat.id, send_fun_sticker)
        bot.send_message(call.message.chat.id, currency.exchange_rate)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=None)

    if call.data == "nene":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=None)
        bot.send_sticker(call.message.chat.id, send_mad_sticker)
        bot.send_message(call.message.chat.id, "Не пиши мне больше", reply_markup=None)


def save_logs1(message):
    time = datetime.datetime.now(tz=pytz.timezone('Etc/GMT-2')).strftime("%d-%m-%Y, %H:%M:%S")
    logs = f'{time} US_name = {message.from_user.first_name}, ID = {message.chat.id} Message_text = {message.text}\n'
    if os.path.exists('logs.txt'):
        with open('logs.txt', "a", encoding="utf-8") as file:
            file.write(logs)
    else:
        with open('logs.txt', "w", encoding="utf-8") as file:
            file.write(logs)


if __name__ == '__main__':
    bot.polling()
