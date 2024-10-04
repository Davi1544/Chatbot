import maritalk
import unidecode
import const as const
import Randomword as rd

class Maritaca:
    def __init__(self, model=None, prompt=""):
          '''
            key : Chave da api do bot;
            prompt: prompt few-shot maritaca;
            '''

          self.model = model
          self.prompt = prompt

    def accumulatePrompt(self,escolhidas,feedbacks) -> str:
        '''
        essa função faz o bot chutar uma palavra com base na dica passda , e retorna essa palavra;
        tip : (String) dica passada para o bot advinhar a palavra;
        return : (String) retorna a palavra que o bot chutou;

        '''
        self.prompt = const.PROMPT_MARITACA

        proibidas = set()
        posicionadas = ["","","","",""]
        tem = set()

        i = 0
        for palavra in escolhidas:
            palavra = list(palavra)

            j = 0
            for letra in palavra:
                if feedbacks[i][j] == "Y":
                    posicionadas[j] = letra
                if feedbacks[i][j] == "M":
                    tem.add(letra)
                if feedbacks[i][j] == "N":
                    if(letra != " "):
                        proibidas.add(letra)
                j += 1
            i += 1

        i = 0
        for letra in posicionadas:
            if(letra != ""):
                self.prompt += "\n A " + const.ORDER[i] + " letra da palavra é " + letra
            i += 1

        if(len(proibidas) > 0):
            self.prompt += "\n As letras proibidas são: "
            for letra in proibidas:
                self.prompt += letra + " "

        if(len(tem) > 0):
            self.prompt += "\n A palavra tem as seguintes letras: "
            for letra in tem:
                self.prompt += letra + " "
        
        print(self.prompt)

        return

    def getWord(self, escolhidas, total, rd) -> str:
        answer = ""
        i = 0
        while (len(answer) != 5 or answer in escolhidas or not rd.is_in(answer)) and i <= 5:
            i += 1
            answer = self.model.generate(
                self.prompt + "\nResposta:", 
                chat_mode=False,
                do_sample=False,
                stopping_tokens=["\n"]
            )["answer"]

            answer = unidecode.unidecode(answer)
            answer = answer.lower()

        print(i)
        if(i > 5):
           answer = rd.pick(total)

        return answer






