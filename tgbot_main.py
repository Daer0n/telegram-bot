from argparse import ArgumentParser
from src.simulation import Simulation
from src.utils import FileUtils
import telebot

bot = telebot.TeleBot('your token')

@bot.message_handler(commands=['start'])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/init', '/help')
    user_markup.row('/watering', '/rain')
    user_markup.row('/drought', '/fertiliser')
    user_markup.row('/weeding', '/insects')
    mess = f"Hello, {message.from_user.first_name}\n" \
           f"This telegram bot implements a model of a garden plot, " \
           f"which implements the cultivation of plants in a garden plot, " \
           f"depending on weather conditions and pests\n" \
           f"/help"
    bot.send_message(message.from_user.id, mess, reply_markup=user_markup)

@bot.message_handler()

def get_user_text(message):
    if message.text == "/init":
        init(message)
    elif message.text == "/help":
        help(message)
    elif message.text == "/drought":
        drought(message)
    elif message.text == "/rain":
        rain(message)
    elif message.text == "/watering":
        watering(message)
    elif message.text == "/fertiliser":
        fertiliser(message)
    elif message.text == "/weeding":
        weeding(message)
    elif message.text == "/insects":
        insects(message)
    else:
        mess = f"I can help you create and manage a model of a garden plot\n\n" \
               f"/help"
        bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=['help'])
def help(message):
    info = str()
    info += f"/init - create garden with 5 seeds.\n" \
            f"/watering - water the garden\n" \
            f"/rain - summon mushroom rain\n" \
            f"/drought - summon the burning sun\n" \
            f"/fertiliser - water the garden with fertilizer\n" \
            f"/weeding - weed the garden\n" \
            f"/disease - summon harmful insects\n"

    bot.send_message(message.chat.id, info, parse_mode="html")

@bot.message_handler(commands=['init'])
def init(message):
    Simulation.init(5)
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")

@bot.message_handler(commands=['drought'])
def drought(message):
    Simulation.run('d')
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")

@bot.message_handler(commands=['rain'])
def rain(message):
    Simulation.run('r')
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")

@bot.message_handler(commands=['watering'])
def watering(message):
    Simulation.run('w')
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")

@bot.message_handler(commands=['fertiliser'])
def fertiliser(message):
    Simulation.run('f')
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")

@bot.message_handler(commands=['weeding'])
def weeding(message):
    Simulation.run('e')
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")

@bot.message_handler(commands=['insects'])
def insects(message):
    Simulation.run('i')
    s = Simulation.from_dict(FileUtils.read_from_json('./state.json'))
    bot.send_message(message.chat.id, s.info_to_str(), parse_mode="html")




bot.polling(none_stop=True)