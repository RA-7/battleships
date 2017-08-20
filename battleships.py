from random import randint


class Battleships:
    def __init__(self, turns=4):
        self.turns = turns
        self.board = []

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def draw_board(self):
        for x in range(5):
            self.board.append(['O'] * 5)

        def random_row():
            return randint(0, len(self.board) - 1)

        def random_col():
            return randint(0, len(self.board) - 1)

        self.ship_row = random_row()
        self.ship_col = random_col()

    def play(self):
        self.draw_board()
        print('Let\'s play Battleships!')
        self.print_board()

        turn = 0

        for _ in range(self.turns):
            turn += 1
            print('Turn {}'.format(turn))
            guess_row = int(input('Guess Row:')) - 1
            guess_col = int(input('Guess Col:')) - 1

            if guess_row == self.ship_row and guess_col == self.ship_col:
                print('You sunk my battleship!')
                break
            else:
                if (guess_row < 0 or guess_row > 4) \
                        or (guess_col < 0 or guess_col > 4):
                    print('That\'s not in the ocean.')
                elif(self.board[guess_row][guess_col] == 'X'):
                    print('You guessed that already.')
                else:
                    print('You missed!')
                    self.board[guess_row][guess_col] = 'X'
                self.print_board()
                if turn == self.turns:
                    print('Game Over')


if __name__ == '__main__':
    game = Battleships()
    game.play()
