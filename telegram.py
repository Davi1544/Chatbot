import telebot
from dotenv import load_dotenv
import os
import termo as termo
import const as const



# funções
def escreva(bot, messageObj, mensagem):
    bot.reply_to(messageObj, mensagem)

def pede_palavra_usuario(bot, message, palavras_escolhidas):
    """
    Pede uma palavra de 5 letras, cofere se tem 5 letras e pede até receber. A função tbm confere se a palavra já não foi escolhida
    SAÍDA: devolve a palavra
    """
    try:
        command, word = message.text.split(maxsplit=1)
        word = word.upper()
        if len(word) != 5:
            bot.reply_to(message, "Palavra inválida, tente novamente")
        elif word in palavras_escolhidas:
            bot.reply_to(message, "Palavra já escolhida, tente novamente")
        else:
            return word   
    except ValueError:
        bot.reply_to(message, "Escolha uma palavra e tente novamente")




def mostra_jogo(bot, message, palavras_escolhidas, feedback):
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
    output = []
    feedback_emoji = []
    bot.reply_to(message, "SEU JOGO ATÉ O MOMENTO\n \n")
    for i in range (len(palavras_escolhidas)):
        new_feedback = ""
        for j in range (len(feedback[i])):
            if (feedback[i][j] == "Y"):
                new_feedback += "✅"
            elif (feedback[i][j] == "N"):
                new_feedback += "❌"
            else:
                new_feedback += "⚠️"
        feedback_emoji.append(new_feedback)
        word = "   ".join([palavras_escolhidas[i][j] for j in range(len(palavras_escolhidas[0]))]) + "\n" + feedback_emoji[i]
        output.append(word)
        bot.send_message(message.chat.id, output[i])
    
def nao_conheco():
    """
        Se por quaisquer motivos, a palavra digitada pelo usuário não é reconhecida, então essa função será chamada.
        Imprima algo nas linhas de: Não conheco essa palavra, ou ela não segue as regras do jogo =( 
    """
