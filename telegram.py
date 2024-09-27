import telebot
from dotenv import load_dotenv
import os
import termo as termo
import const as const

# setup basico
load_dotenv()
CHAVE_TELEGRAM = os.getenv("CHAVE_TELEGRAM")
bot = telebot.TeleBot(CHAVE_TELEGRAM)

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