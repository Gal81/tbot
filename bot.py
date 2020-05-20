import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(
    message.chat.id,
    'Hi there! <b>{0.first_name}</b>'.format(message.from_user, bot.get_me()),
    parse_mode='html'
  )

@bot.message_handler(content_types=['text'])
def botTalk(message):
  bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)
