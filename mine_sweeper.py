import random



class Board:
    def __init__(self,dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs


        self.board = self.make_new_board()
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]



        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size**2 -1)
            row = loc // self.dim_size

            if board[row][col] == '*':

def play(dim_size=10, num_bombs=10):
