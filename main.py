# first steps
import os

import maritalk

from dotenv import load_dotenv

load_dotenv()

chave = os.getenv("CHAVE")

model = maritalk.MariTalk(
    key=chave,
    model="sabia-3"  # No momento, suportamos os modelos sabia-3, sabia-2-medium e sabia-2-small
)






#pergunta do usuario
user_question = input()

question = model.generate(user_question, max_tokens=200)

answer = question["answer"]

print(f"Resposta: {answer}")
    

while(True):
    #pega o antigo contexto da conversa
    user_question = input()

    history = [
        {"role": "user", "content": user_question},
        {"role": "assistant", "content": "irei escrever uma palavra,que termina com a mesma vogal que a sua!"}  # Aqui você adiciona a resposta anterior do modelo
        ]

    question = model.generate(history, max_tokens=200)

    answer = question["answer"]

    print(f"Resposta: {answer}")
    









question = model.generate(history, max_tokens=200)

answer = question["answer"]


print(f"Resposta: {answer}")










