import telebot
import requests

# Токен Telegram-бота
bot = telebot.TeleBot("7618850095:AAHhkzF1y1G2NtOup195bcimW8jCVzNUivk")

RANDOM_USER_API = "https://randomuser.me/api/"

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        "Привет! Напиши /photo, чтобы получить случайное фото человека."
    )

@bot.message_handler(commands=['photo'])
def send_random_user_photo(message):
    try:
        response = requests.get(RANDOM_USER_API)
        if response.status_code == 200:
            data = response.json()
            photo_url = data['results'][0]['picture']['large']
            
            bot.send_photo(message.chat.id, photo_url, caption="Вот случайное фото человека!")
        else:
            bot.send_message(message.chat.id, "Ошибка при получении фото. Попробуйте позже.")
    except requests.RequestException:
        bot.send_message(message.chat.id, "Не удалось подключиться к серверу. Попробуйте позже.")

# Запуск бота
bot.polling()