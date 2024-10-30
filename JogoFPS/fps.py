class Jogador:
    energia: float

    def __init__(self):
        self.energia = 150
        
    def __str__(self):
        return f'Energia: {self.energia}'