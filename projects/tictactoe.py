# Tic Tac Toe
# This is a two player game
# Player one is X, player two is O
# They take turns picking a position on the board


class TicTacToe:
    '''Tic Tac Toe happens here'''
    def __init__(self, size):
        '''Generate a board of the given width and height'''
        self.size = size
        self.board = [str(i) for i in list(range(self.size * self.size))]
        self.player = 'X'
        self.stop = False

    def display(self):
        '''Print the board to the console'''
        for line in range(0, self.size * self.size, self.size):
            row = self.board[line : line + self.size]
            print(row)

    def turn(self):
        '''Make the player choose a position, fill it in on the board, swap who's playing'''
        position = input(f"Player {self.player}, choose a position: ")

        if position == 'exit':
            self.stop = True
            return False

        if position not in self.board:
            print(f"Can't choose this position, try again")
            return True

        self.board[int(position)] = self.player
        self.player = 'X' if self.player == 'O' else 'O'

    def check(self):
        '''Check whether the game has been won'''
        winner = None

        if all(i in {'X', 'O'} for i in self.board):
            winner = 'TIE'

        for row in range(0, self.size * self.size, self.size):
            row = self.board[row : row + self.size]

            if all(i == 'X' for i in row):
                winner = 'X'

            elif all(i == 'O' for i in row):
                winner = 'O'

        for col in range(0, self.size):
            col = self.board[col :: self.size]

            if all(i == 'X' for i in col):
                winner = 'X'

            elif all(i == 'O' for i in col):
                winner = 'O'

        dia = self.board[:: self.size + 1]

        if all(i == 'X' for i in dia):
            winner = 'X'

        if all(i == 'O' for i in dia):
            winner = 'O'

        dia = self.board[self.size - 1 : self.size * self.size - 1 : self.size - 1]

        if all(i == 'X' for i in dia):
            winner = 'X'

        if all(i == 'O' for i in dia):
            winner = 'O'

        if winner in {'X', 'O'}:
            print(f"Player {winner} won!")
            return True

        elif winner == 'TIE':
            print(f"The game was a tie!")
            return True

    def start(self):
        '''Start the game of tic tac toe'''
        while True:
            self.display()

            if self.check():
                break

            while(self.turn()):
                pass

            if self.stop:
                self.stop = False
                break

    def reset(self):
        self.board = [str(i) for i in list(range(self.size * self.size))]
        self.player = 'X'


tictactoe = TicTacToe(3)
tictactoe.start()
