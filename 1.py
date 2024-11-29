import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import API

bot = telebot.TeleBot(API)

# Команда /start для создания кнопок выбора
@bot.message_handler(commands=['start'])
def welcome_user(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Тестирование"))
    markup.add(KeyboardButton("Разработка"))
    markup.add(KeyboardButton("Дизайн"))
    bot.send_message(
        message.chat.id,
        "Привет! Выберите одну из категорий:",
        reply_markup=markup
    )

# Обработка сообщений с текстом
@bot.message_handler()
def send_category_links(message):
    if message.text == "Тестирование":
        bot.send_message(
            message.chat.id,
            """<b>Ресурсы для тестировщиков:</b>
1. <a href="https://www.softwaretestinghelp.com/">Software Testing Help</a> - статьи и руководства по тестированию ПО.
2. <a href="https://testguild.com/">TestGuild</a> - подкасты и блоги по автоматизации тестирования.
3. <a href="https://www.ministryoftesting.com/">Ministry of Testing</a> - сообщество тестировщиков и обучающие материалы.""",
            parse_mode="HTML"
        )
    elif message.text == "Разработка":
        bot.send_message(
            message.chat.id,
            """<b>Ресурсы для разработчиков:</b>
1. <a href="https://stackoverflow.com/">Stack Overflow</a> - сообщество разработчиков и решение проблем.
2. <a href="https://github.com/">GitHub</a> - хранилище кода и проектов.
3. <a href="https://dev.to/">DEV Community</a> - статьи и обсуждения для программистов.""",
            parse_mode="HTML"
        )
    elif message.text == "Дизайн":
        bot.send_message(
            message.chat.id,
            """<b>Ресурсы для дизайнеров:</b>
1. <a href="https://dribbble.com/">Dribbble</a> - портфолио и вдохновение для дизайнеров.
2. <a href="https://www.behance.net/">Behance</a> - платформа для креативных работ.
3. <a href="https://uxdesign.cc/">UX Design</a> - статьи и советы по UX/UI-дизайну.""",
            parse_mode="HTML"
        )
    else:
        bot.send_message(message.chat.id, "Извините, я не понимаю ваш запрос.")

# Запуск бота
bot.polling()