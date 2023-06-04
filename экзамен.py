import telebot
import random

from telebot import types

bot = telebot.TeleBot("6271102429:AAGAcA7cAh4Kvp0Pakd1sYoYMPfS9NbaEkA")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Stiker2.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Когда домой ")
    item2 = types.KeyboardButton("Какая оценка по экзамену")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,f"Приветствую мой господин я телеграм бот у меня есть несколько команд чтоб их узнать напишите /help и я вам все ракажу, {message.from_user.first_name}!")

@bot.message_handler(commands=['1'])
def welcome(message):
    bot.send_message(message.chat.id," змея споткнулась")

@bot.message_handler(commands=['2'])
def send_welcome(message):
    stiq = open('2.webp','rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,"/start (это команда нужна чтоб начать общение со мной ) /1 (эта комана нужна если вам стало скучно и я вам раскажушутку) /2 (эта команда покажет вам смешную картинку)/3(музыка)")
@bot.message_handler(commands=['3'])
def send_music(message):
    audio = open('asd.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text.lower() == "что делаешь":
        bot.send_message(message.chat.id, 'делаю уроки, а ты')

    if message.text.lower() == "какую оценку хочешь":
        bot.send_message(message.chat.id, str(random.randint(1,12)))

    if message.text.lower() == "как дела":
        bot.send_message(message.chat.id, 'хорошо')

    if message.text.lower() == "ты любишь кушать":
        bot.send_message(message.chat.id, 'я не могу кушать я робат')

    if message.text.lower() == "что ты любишь":
        bot.send_message(message.chat.id, 'я люблю с вами общяться')

    if message.text.lower() == "что ты не любишь":
        bot.send_message(message.chat.id, 'я не люблю спам')

    if message.text.lower() == "ты спишь":
        bot.send_message(message.chat.id, 'Нет')

    if message.text.lower() == "у тебя есть друзья":
        bot.send_message(message.chat.id, 'да есть один друг')

    if message.text.lower() == "а как зовут твоего друга":
        bot.send_message(message.chat.id, 'я не скажу это сикрет!!!')

    if message.text.lower() == "ты можешь сделать домашку":
        bot.send_message(message.chat.id, 'нет я занят думай сам !')






bot.polling ()
