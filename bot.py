import telebot

bot = telebot.Telebot('1079190137:AAFcTWcmKiTPEmAUowbL1pdN3jw1YzSUrFY')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()