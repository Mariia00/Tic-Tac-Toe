import math
import random

class Player:
    def __init__(self, letter):
        # буква X або O
        self.letter = letter
    
    # ми хочемо, щоб усі гравці зробили наступний хід у грі
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # отримати випадкове дійсне місце для нашого наступного кроку
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game): 
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # ми перевіримо, чи це правильне значення, спробувавши привести
            # це до цілого числа, і якщо це не так, ми кажемо, що воно недійсне
            # якщо ця точка недоступна на дошці, ми також кажемо, що вона недійсна
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError 
                valid_square = True # якщо вони будуть успішними, тоді ура!
            except ValueError:
                print('Invalid square. Try again')

        return val

     

