import telebot

bot = telebot.TeleBot(API)


user_data = {}

@bot.message_handler(commands=['start'])
def start_dialog(message):
    user_data[message.chat.id] = {}  # Инициализация данных для пользователя
    bot.send_message(message.chat.id, "Как тебя зовут?")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id

    # Проверяем этап диалога
    if 'name' not in user_data[chat_id]:
        user_data[chat_id]['name'] = message.text
        bot.send_message(chat_id, f"Тебя зовут {message.text}. Сколько тебе лет?")
    elif 'age' not in user_data[chat_id]:
        user_data[chat_id]['age'] = message.text
        bot.send_message(chat_id, f"Тебе {message.text} лет. Где ты живешь?")
    elif 'location' not in user_data[chat_id]:
        user_data[chat_id]['location'] = message.text
        bot.send_message(chat_id, f"Ты живешь в {message.text}. Спасибо за ответы!")
    else:
        bot.send_message(chat_id, "Мы уже закончили диалог. Напиши /start, чтобы начать заново.")

bot.polling()