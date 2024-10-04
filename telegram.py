import telebot
from unidecode import unidecode
#from dotenv import load_dotenv
import os
import termo as termo
import const as const

class telegram:
    def __init__(self, bot=None, messageObj=None):
        self.bot = bot
        self.messageObj = messageObj

    # funções
    def escreva(self, mensagem):
        self.bot.reply_to(self.messageObj, mensagem)

    def pede_palavra_usuario(self, palavras_escolhidas):
        """
        Pede uma palavra de 5 letras, cofere se tem 5 letras e pee até receber. A função tbm confere se a palavra já não foi escolhida
        SAÍDA: devolve a palavra
        """


    def mostra_jogo(self, palavras_escolhidas, feedback, fim, ehMari):
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
        
        if(ehMari): 
            mensagem = """Segue o jogo da Maritaca\t\t: \n\n"""
        else:
            mensagem = """Seu jogo até o momento\t\t: \n\n"""
        i = 0
        for palavra in palavras_escolhidas:
            palavra = unidecode(palavra)
            palavra = list(palavra)

            for letra in palavra:
                cod = ord(letra) - 97 
                if(cod >= 0 and cod <= 25):
                    mensagem += const.alphabet[cod] + "     "
                else:
                    mensagem += "\U00002753" + "  "

                #print(str(cod) + " : " + const.alphabet[cod])
            mensagem += "\n"

            for feedletra in feedback[i]:
                color = const.colors[feedletra]
                mensagem += color + "  "
            mensagem += "\n\n"

            i += 1
                
        # 1 => user ganhou
        # 2 => maritaca ganhou
        if(fim == 1 and not ehMari):
            mensagem += "Você ganhou!!!!!\nUse /aigame para ver o jogo da maritaca."

        if(fim == 2 and not ehMari):
            mensagem += "Você perdeu. A maritaca ganhou =("

        self.escreva(mensagem)

    def nao_conheco(self):
        """
            Se por quaisquer motivos, a palavra digitada pelo usuário não é reconhecida, então essa função será chamada.
            Imprima algo nas linhas de: Não conheco essa palavra, ou ela não segue as regras do jogo =( 
        """

        mensagem = "Não conheco essa palavra, ou ela não segue as regras do jogo =("
        self.escreva(mensagem)