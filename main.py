import maritalk
import telebot
from dotenv import load_dotenv
import os

import termo as termo
import const as const
import telegram as telegram
import Randomword as rd
import Maritaca as maritaca

# setup game
game = termo.Termo()
random = rd.Randomword("files/words.txt")

if __name__ == "__main__":
    # setup basico
    load_dotenv()
    CHAVE_MARITACA = os.getenv("CHAVE_MARITACA")
    CHAVE_TELEGRAM = os.getenv("CHAVE_TELEGRAM")
    model = maritalk.MariTalk(
        key=CHAVE_MARITACA,
        model="sabia-3"
    )
    bot = telebot.TeleBot(CHAVE_TELEGRAM)

    # telegram
    def restart_attempt(message):
        global bot
        telegram.escreva(bot, message, const.MENSAGEM_RESTART_ATTEMPT)

    @bot.message_handler(commands=["start"])
    def start(message):
        global bot
        game = termo.Termo()
        telegram.escreva(bot, message, const.MENSAGEM_ENTRADA)
    
    @bot.message_handler(commands=["smashai"])
    def start(message):
        global bot, random

        if(game.palavra != ""):
            restart_attempt(message)

        palavra = random.getWord()
        game.palavra = palavra
        telegram.pede_palavra_usuario(bot, game.user["escolhidas"])

    @bot.message_handler(commands=["restart"])
    def start(message):
        start()

    @bot.message_handler(func=lambda message: True)
    def jogo(message):
        global bot

        print(message.text)

    bot.infinity_polling()