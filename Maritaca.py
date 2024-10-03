import maritalk


class Maritaca:
    model = 0

    def __init__(self, key, prompt):
        '''
            key : Chave da api do bot;
            prompt: prompt few-shot maritaca;
            '''

        self.__key = key
        self.prompt = prompt

    def start_maritaca(self):
        '''
            essa função inicializa o modelo da maritaca;
        '''
        global model
        model = maritalk.MariTalk(
            key=self.__key,
            model="sabia-3"
        )

    def getAnswer(self, feedback, previous_answer):
        ''' essa funcao recebe um feedback e com base no feedback   faz  e
        o bot chutar uma palavra, e retorna essa palavra.
        previous_answer : (String) palavra anterior chutada pelo bot.
        feedback : (String) feedback para ser transformado em dicas
        return : (String) retorna a palavra que o bot chutou; '''
        tip = ""  # dica que vai ser passado para o bot

        # se não tiver feedback , não possuo dicas
        if len(feedback) > 0:
            for i in range(len(feedback)):
                if feedback[i] == "Y":
                    tip += f"A palavra possui a letra  '{previous_answer[i]}' na posição {i + 1} da palavra."
                elif feedback[i] == "N":
                    tip += f"A palavra não possui a letra  '{previous_answer[i]}'."
                elif feedback[i] == "M":
                    tip += f"A palavra  possui a letra '{previous_answer[i]}',porém está na posição errada."
        else:
            tip = "Não há dicas disponíveis ainda."

        if tip == "Não há dicas disponíveis ainda.":
            self.prompt += tip + "\n Resposta:"
            answer = model.generate(self.prompt, max_tokens=200)["answer"]
            self.prompt += answer + "\n Dica:"
        else:
            self.prompt += tip + "\n Resposta:"
            answer = model.generate(self.prompt, max_tokens=200)["answer"]
            self.prompt += answer + "\n Dica:"
        return answer
