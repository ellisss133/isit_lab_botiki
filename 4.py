import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = telebot.TeleBot("7618850095:AAHhkzF1y1G2NtOup195bcimW8jCVzNUivk")

# Команда /start: создаем клавиатуру
@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Кнопка 1"), KeyboardButton("Кнопка 2"))
    markup.add(KeyboardButton("Закрыть"))
    bot.send_message(message.chat.id, "Вот ваша клавиатура. Напишите 'Закрыть', чтобы её убрать.", reply_markup=markup)

# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text.lower() == "закрыть":
        bot.send_message(message.chat.id, "Клавиатура удалена.", reply_markup=ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, f"Вы написали: {message.text}")

# Запуск бота
bot.polling()