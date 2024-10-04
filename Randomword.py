import random

class Randomword:

    def __init__(self, file):

        self.file = file


    def getWord(self):
        """essa funcao le uma palavra aletoria do arquivo e a retorna
            Return : String word
        """

        arraywords = []
        with open(self.file,'r') as file:
            for line in file:
                arraywords.append(line.strip())

        randomN = random.randint(0,len(arraywords)-1) 

        word = arraywords[randomN]
        
        return word

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
