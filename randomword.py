import random
import unidecode

class Randomword:

    def __init__(self, file):

        self.file = file


    def returnAll(self):
        arraywords = []
        with open(self.file,'r') as file:
            for line in file:
                arraywords.append(line.strip())
        
        return arraywords
    
    def pick(self, total):
        """essa funcao le uma palavra aletoria do arquivo e a retorna
            Return : String word
        """

        randomN = random.randint(0,len(total)-1) 

        word = total[randomN]
        
        return word

    def criaPosicionadas(self,escolhidas,feedbacks) -> str:
        '''
        cria vetor de letras já posicionadas

        '''
        posicionadas = ["","","","",""]

        i = 0
        for palavra in escolhidas:
            palavra = list(palavra)

            j = 0
            for letra in palavra:
                if feedbacks[i][j] == "Y":
                    posicionadas[j] = letra
                j += 1
            i += 1

        return posicionadas
    
    def selectFew(self, total, letters):
        arraywords = []
        for line in total:
            line = list(line)

            for i in range(5):
                if(line[i] != letters[i] and letters[i] != ""):
                    break

                # garante que a palavra segue as regras
                if(i == 4):
                    arraywords.append(line.strip())

        return arraywords

    def is_in(self, palavra):
        """
            Checa se uma palavra está no arquivo
        """

        arraywords = []
        with open(self.file, 'r', encoding='utf-8') as file:
            for line in file:
                arraywords.append(line.strip())
                
        if palavra in arraywords:
            return True
        else:
            return False
