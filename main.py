import maritalk
import telebot
from dotenv import load_dotenv
import os

import termo as termo
import const as const
import telegram as telegram
import Randomword as random
import Maritaca as maritaca

# setup game
game = termo.Termo()

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
    @bot.message_handler(commands=["start"])
    def start(message):
        global bot

        game = termo.Termo()
        telegram.escreva(bot, message, const.MENSAGEM_ENTRADA)
    
    @bot.message_handler(commands=["smashai"])
    def start(message):
        global bot

        palavra = random.getWord()
        game.palavra = palavra
        print(palavra)

    bot.infinity_polling()