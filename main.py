import maritalk
import telebot
import unidecode
from dotenv import load_dotenv
import os

import termo as termo
import const as const
import telegram as telegram
import Randomword as rd
import Maritaca as mari

# setup game
game = termo.Termo()
random = rd.Randomword("files/words.txt")
tele = telegram.telegram()
maritaca = mari.Maritaca()

suporte_maritaca = []

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
    tele.bot = bot

    maritaca.model = model
    maritaca.prompt = const.PROMPT_MARITACA

    # telegram
    def set(message):
        tele.messageObj = message
        return
    
    def restart_attempt(message):
        set(message)
        tele.escreva(const.MENSAGEM_RESTART_ATTEMPT)

    def preparaMaritaca():
        primeira_letra = list(game.palavra)
        primeira_letra = primeira_letra[0]

        dica1 = primeira_letra + "    "
        feed1 = ["Y", "N", "N", "N", "N"]
        game.maricata["escolhidas"].append(dica1)
        game.maricata["feedbacks"].append(feed1)

    @bot.message_handler(commands=["start"])
    def start(message):
        set(message)

        game = termo.Termo()
        tele.escreva(const.MENSAGEM_ENTRADA)
    
    @bot.message_handler(commands=["smashai"])
    def smash(message):
        set(message)

        if(game.palavra != ""):
            restart_attempt(message)
            return

        suporte_maritaca = random.returnAll()
        palavra = random.pick(suporte_maritaca)
        game.palavra = palavra
        preparaMaritaca()
        tele.pede_palavra_usuario(game.user["escolhidas"])

    @bot.message_handler(commands=["restart"])
    def restart(message):
        start(message)

    @bot.message_handler(commands=["aigame"])
    def aigame(message):
        tele.mostra_jogo(game.maricata["escolhidas"], game.maricata["feedbacks"], game.fim, True)

    @bot.message_handler(func=lambda message: True)
    def jogo(message):
        set(message)

        if game.palavra == "":
            tele.escreva(const.MENSAGEM_NO_GAME_WORD)
            return
        
        # considerando que o jogo já foi iniciado
        digitado = message.text
        digitado = unidecode.unidecode(digitado)
        digitado = digitado.lower()

        if(not game.trata_palavra(random, digitado)):
            tele.nao_conheco()
            return

        # considerando que a palavra é válida
        if(game.fim == 0):
            game.julga_palavra(True, digitado)
            tele.escreva(const.WAIT)

            posicionadas = random.criaPosicionadas(game.maricata["escolhidas"], game.maricata["feedbacks"])
            suporte_maritaca = random.selectFew(suporte_maritaca, posicionadas)

            maritaca.accumulatePrompt(game.maricata["escolhidas"], game.maricata["feedbacks"])
            resposta_maritaca = maritaca.getWord(game.maricata["escolhidas"], suporte_maritaca, random)
            game.julga_palavra(False, resposta_maritaca)

        tele.mostra_jogo(game.user["escolhidas"], game.user["feedbacks"], game.fim, False)

        if(game.fim == 2):
            tele.mostra_jogo(game.maricata["escolhidas"], game.maricata["feedbacks"], game.fim, True)

        print([game.palavra])
        print(game.user["escolhidas"])
        print(game.user["feedbacks"])
        print(game.maricata["escolhidas"])
        print(game.maricata["feedbacks"])

    bot.infinity_polling()