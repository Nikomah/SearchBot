import telebot
import parser
from tokenbot import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, f'Привет, {message.from_user.first_name}. Посмотреть свежие заказы? (да/нет)?')
    bot.register_next_step_handler(msg, ask_pars)


def ask_pars(message):
    text = message.text.lower()
    chat_id = message.chat.id

    if text == 'нет':
        bot.send_message(chat_id, 'Ок, тогда отдыхаем. Если они всё же понадобятся, просто набери "да".')
    elif text == 'да':
        output = parser.parse_content()
        # print(output)
        bot.send_message(chat_id, '\n'.join(output))
    else:
        bot.send_message(chat_id, 'Я понимаю только да или нет')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'привет':
        bot.send_message(chat_id, 'Привет и тебе!')
    elif text == 'давай поболтаем':
        bot.send_message(chat_id, 'Некогда болтать, давай лучше поработаем')
    elif text == 'да':
        output = parser.parse_content()
        bot.send_message(chat_id, '\n'.join(output))
    else:
        bot.send_message(chat_id, 'Не понимаю, что ты говоришь')


bot.infinity_polling()
