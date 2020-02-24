import telebot
import requests

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, это погодный бот:)\nНапиши город (на английском) и я покажу погоду.')

@bot.message_handler(content_types=['text'])
def weather_message(message):
    city = message.text.lower()
    weather_key = 'KEY'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&lang=ru&units=metric&appid=' + weather_key

    res = requests.get(weather_url.format(city)).json()

    if res['cod'] == 200:
        bot.send_message(message.chat.id, 'Город: {}\nCостояние погоды: {}\nТемпература: {}'.format(res['name'], res['weather'][0]['description'], res['main']['temp']))
    else:
        bot.send_message(message.chat.id, 'Город неправильно введен или такого города нет:(')

bot.polling()
