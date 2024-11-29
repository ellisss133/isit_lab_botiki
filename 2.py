import telebot

bot = telebot.TeleBot("7618850095:AAHhkzF1y1G2NtOup195bcimW8jCVzNUivk")

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    bot.reply_to(message, "спс за гс😘")

bot.polling()