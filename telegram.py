import telebot
from dotenv import load_dotenv
import os
import termo as termo
import const as const

# funções
def escreva(bot, messageObj, mensagem):
    bot.reply_to(messageObj, mensagem)