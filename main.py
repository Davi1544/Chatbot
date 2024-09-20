import maritalk
import telebot
from dotenv import load_dotenv
import os

import termo as termo
import const as const

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

    # criando objeto jogo
    game = termo.Termo()

    # funções
    def escreva(messageObj, mensagem):
        bot.reply_to(messageObj, mensagem)

    def sorteiePalavraIA() -> str:
        palavra = model.generate(
            const.IA_MENSAGEM_PALAVRA_5,
            chat_mode=False,
            do_sample=False,
            stopping_tokens=["\n"]
        )["answer"]

        print(palavra)

        return palavra

    # telegram
    @bot.message_handler(commands=["start"])
    def start(message):
        game = termo.Termo()
        escreva(message, const.MENSAGEM_ENTRADA)
    
    @bot.message_handler(commands=["smashai"])
    def start(message):
        palavra = sorteiePalavraIA()
        escreva(message, palavra)

    bot.infinity_polling()