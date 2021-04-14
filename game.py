from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        # use a single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of winner

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (which number corresponds to which box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid assign square to letter
        # return true else return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True

        return False

    def winner(self, square, letter):
        # winner if 3 in a row
        # check row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # only if square is an even number (0, 2, 4, 6, 8)
        # only move possible to win diagonally
        if square % 2 == 0:
            diagonal_left_right = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_left_right]):
                return True
            diagonal_right_left = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_right_left]):
                return True

        # if all fails
        return False


def play(game, x_player, o_player, print_game=True):
    # return the winner or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # print line

        # check for winner
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter

        # alternate players
        letter = 'O' if letter == 'X' else 'X'

        if print_game:
            print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
