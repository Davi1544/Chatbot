import maritalk
import telebot
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    CHAVE_MARITACA = os.getenv("CHAVE_MARITACA")
    CHAVE_TELEGRAM = os.getenv("CHAVE_TELEGRAM")

    model = maritalk.MariTalk(
        key=CHAVE_MARITACA,
        model="sabia-3"
    )

    bot = telebot.TeleBot(CHAVE_TELEGRAM)

    @bot.message_handler(commands=["start"])
    def bem_vindo(message):
        bot.reply_to(
            message, "Começando....")

        # TODO: pedir pro maritaca uma palavra boa de 5 letras aleatória
        # TODO: salvar essa palavra aleatória no estado da classe ou em variável global

    @bot.message_handler(func=lambda message: True)
    def resposta(message):

        # TODO: falar para a martica julgar o chute em relação a palavra real
        # OU implementar o algorítmo de comparação de palavras na mão

        mensagem = message.text
        mensagem += "\n"
        
        correcao = model.generate(
            mensagem,
            chat_mode=False,
            do_sample=False,
            stopping_tokens=["\n"]
        )["answer"]
        

        bot.reply_to(message, correcao)

    bot.infinity_polling()