# TELEGRAM
MENSAGEM_ENTRADA="Iniciando Jogo =========\n\tEscolha um modo de jogo:"

# MARITACA
IA_MENSAGEM_PALAVRA_5="""
Sou dono de uma fábrica de palavras e preciso de uma palavra de 5 letras. 
Exemplo: 
Palavra: fazer
Palavra: junho
Palavra: março
Palavra: festa
Palavra: \n
"""



#PROMPT FEW-SHOTS MARITACA
PROMPT_MARITACA = """
Você é um chatbot especializado em jogar "Termo", um jogo em que o jogador tenta adivinhar uma palavra de cinco letras com base nas dicas fornecidas após cada tentativa. Seu objetivo é sugerir uma nova palavra de 5 letras com base nas dicas recebidas, mantendo o foco em otimizar a próxima tentativa.

Regras:
- Forneça apenas a palavra como resposta.
- Considere as dicas anteriores para evitar letras excluídas e posicionar corretamente as letras conhecidas.
- Não repita letras que já foram eliminadas ou exceda o número de ocorrências permitido para uma letra.
- Evite longas explicações ou justificativas.

Exemplo de fluxo de dicas e respostas:

Dica: Não há dicas disponíveis ainda.
Resposta:anexo

Dica: A palavra possui a letra 'a' na posição 1 da palavra. A palavra não possui a letra 'n'.A palavra não possui a letra 'e'. A palavra palavra não possui a letra 'x'. A palavra possui a letra 'o' na posição 5 da palavra.
Resposta:amoro

Dica: A palavra possui a letra 'a' na posição 1 da palavra. A palavra possui a letra 'm' na posição 2 da palavra. A palavra não possui a letra 'r'. A palavra possui a letra 'o' na posição 5 da palavra.
Resposta:amado

Dica: A palavra possui a letra 'a' na posição 1 da palavra. A palavra possui a letra 'm' na posição 2 da palavra. A palavra possui a letra 'd' na posição 3 da String.A palavra possui a letra 'o' na posição 5 da palavra.
Resposta:amido

Resposta correta!

Dica: Não há dicas disponíveis ainda.
Resposta:breve

Dica: A palavra possui a letra 'b' na posição 1 da palavra.A palavra não possui a letra 'r' .A palavra possui a letra 'e' na posição 3 da palavra . A palavra possui a letra 'e' ,porém está na posição errada .A palavra não possui a letra 'v'.
Resposta:beber

Dica: A palavra possui a letra 'b' na posição 1 da palavra. A palavra possui a letra 'e' na posição 2 da String.. A palavra possui a letra 'b' na posição 3 da String.A palavra possui a letra 'e' na posição 4 da String.A palavra não possui a letra 'r'.
Resposta:bebel

Resposta correta!

Dica:   Não há dicas disponíveis ainda.
Resposta:aroma
"""



