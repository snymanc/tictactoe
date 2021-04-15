import time
from player import HumanPlayer, RandomComputerPlayer, AIComputerPlayer


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

        # tiny delay before next move
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie')


def human_play():
    x_player = HumanPlayer('X')
    o_player = AIComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


def computers_play(num_games):
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(num_games):
        x_player = RandomComputerPlayer('X')
        o_player = AIComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)

        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(
        f'After {num_games} simulation\'s, {x_wins} X wins, {o_wins} O wins and {ties} ties')


if __name__ == '__main__':
    game_type = int(input('Game play options:\n\t1 You vs AI\n\t2 AI simulation\n'))
    if game_type == 1:
        human_play()
    elif game_type == 2:
        num_games = int(input('Number of games?\n'))
        computers_play(num_games)
    else:
        f'Invalid option {game_type}'
