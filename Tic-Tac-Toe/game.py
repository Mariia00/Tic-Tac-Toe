import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # ми будемо використовувати один список для повторення дошки 3x3
        self.current_winner = None # стежте за переможцем! 

    def print_board(self):
        # це просто отримання рядків
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (говорить нам, яке число відповідає якій коробці)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # якщо правильний хід, то зробіть хід (призначене букві)
        # потім повертає істину/ якщо недійсний, повертає хибність
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # переможець, якщо 3 поспіль будь-де.. ми повинні перевірити все це!
        # спочатку перевіримо рядок
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # перевірка колонки
        col_ind = square % 3      
        column = [self.board[col_ind + i*3] for i in range(3)] 
        if all([spot == letter for spot in column]):
            return True
        
        # перевірте діагоналі
        # але тільки якщо квадрат є парним числом (0, 2, 4, 8)
        # це єдині ходи, які можна виграти по діагоналі
        if square & 2 ==0:
            diagonal1 = [self.board[i] for i in  [0, 4, 8]] # діагональ зліва направо
            if all([spot == letter for spot in diagonal1]):
                 return True 
            diagonal2 = [self.board[i] for i in  [2, 4, 6]] # справа наліво по діагоналі
            if all([spot == letter for spot in diagonal2]):
                 return True 
            
        # якщо все це не вдасться
        return False          
        
        
    

        
def play(game, x_player, o_player, print_game = True):
    # повертає переможця гри (лист)! або Жодного для краватки
    if print_game:
        game.print_board_nums()

    letter = 'X' # початковий лист
    # повторюйте, поки в грі ще є порожні квадрати
    #(нам не потрібно турбуватися про переможця, тому що ми просто повернемо його
    # що розриває петлю)
    while game.empty_squares():
        # отримати хід від відповідного гравця
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # давайте визначимо функцію, щоб зробити хід!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # просто порожній рядок
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            # після того, як ми зробили свій хід, нам потрібно чергувати літери
            letter = 'O' if letter =='X' else 'X'
            # if letter == 'X':
                # letter = 'O'
            # else:
                # letter = 'X'

        # маленька перерва, щоб полегшити читання
        time.sleep(0.8)


    if print_game:
        print('It\'s a tie!')
            
# для запуску коду в операторі if лише тоді, коли програма запускається безпосередньо інтерпретатором Python
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)













