import telebot
from dotenv import load_dotenv
import os
import termo as termo
import const as const

# funções
def escreva(bot, messageObj, mensagem):
    bot.reply_to(messageObj, mensagem)

def pede_palavra_usuario(bot, palavras_escolhidas):
    """
    Pede uma palavra de 5 letras, cofere se tem 5 letras e pee até receber. A função tbm confere se a palavra já não foi escolhida
    SAÍDA: devolve a palavra
    """


def mostra_jogo(bot, palavras_escolhidas, feedback):
    """A função printa o jogo para o usuário. Ex: finja que a palavra é musgo e o 
        usuário chutou {custo e rácio}. A função receberia
            palavras_escolhidas = ["custo","rácio"]
            feedback = ["NYYNY","NNNNM"]

        ao passo que,
            N => não tem
            Y => tem E está no lugar certo
            M => tem E NÃO está no lugar certo (misplaced)

        Logo, o usuário deveria receber algo como

        SEU JOGO ATÉ O MOMENTO

        C U S T O
        N Y Y N Y

        R Á C I O
        N N N N M

        claro que as letras código virariam emojis, ent vc tem que descobrir como mandar emojis pelo python ={
    """
