
import maritalk

class Maritaca:
 
    model = 0
    
    def __init__(self, key,prompt ):
          '''
            key : Chave da api do bot;
            prompt: prompt few-shot maritaca;
            '''

          self.__key = key
          self.prompt  = prompt
    
    def start_maritaca(self):
        '''
        essa função inicializa o modelo da maritaca;
        '''
        global model    
        model = maritalk.MariTalk(
            key=self.__key,
            model="sabia-3" 
        )
    

    def accumulatePrompt(self,tip):
        '''
        essa função faz o bot chutar uma palavra com base na dica passda , e retorna essa palavra;
        tip : (String) dica passada para o bot advinhar a palavra;
        return : (String) retorna a palavra que o bot chutou;

        '''
        global model
        
        answer = model.generate(self.prompt, max_tokens=200)["answer"]
        
        self.prompt+= tip + "\n Resposta:" 

        answer = model.generate(self.prompt, max_tokens=200)["answer"]

        self.prompt+=  answer  + "\n Dica:"
                
        return answer








