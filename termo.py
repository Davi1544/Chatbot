class Termo:
    def __init__(self, palavra = "", prompt = ""):
        self.palavra = palavra
        self.prompt = prompt

        self.user = {
            "escolhidas": [],
            "feedback": []
        }
        self.maricata = {
            "escolhidas": [],
            "feedback": []
        }