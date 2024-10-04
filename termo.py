import const as const

class Termo:
    def __init__(self, palavra = "", prompt = "", fim=0):
        self.palavra = palavra
        self.prompt = prompt
        self.fim = fim

        self.user = {
            "escolhidas": [],
            "feedbacks": []
        }
        self.maricata = {
            "escolhidas": [],
            "feedbacks": []
        }
    
    def trata_palavra(self, random, palavra) -> bool:

        if len(palavra) != 5:
            return False
        if not random.is_in(palavra):
            return False

        return True

    def julga_palavra(self, user, palavra) -> None:
        goal = self.palavra

        if(goal == palavra):
            if(user == True):
                self.fim = 1
            else:
                self.fim = 2

        feedback = []

        # quebrando a palavra
        goal_split = list(goal)
        palavra_split = list(palavra)

        for i in range(5):
            goal_letra = goal_split[i]
            palavra_letra = palavra_split[i]

            if(goal_letra == palavra_letra):
                feedback.append("Y")
            elif palavra_letra in goal_split:
                feedback.append("M")
            else:
                feedback.append("N")

        
        if(user):
            escolhidas = list(self.user["escolhidas"])
            escolhidas.append(palavra)
            self.user["escolhidas"] = escolhidas

            feedbacks = list(self.user["feedbacks"])
            feedbacks.append(feedback)
            self.user["feedbacks"] = feedbacks

        else:
            escolhidas = list(self.maricata["escolhidas"])
            escolhidas.append(palavra)
            self.maricata["escolhidas"] = escolhidas

            feedbacks = list(self.maricata["feedbacks"])
            feedbacks.append(feedback)
            self.maricata["feedbacks"] = feedbacks

        return