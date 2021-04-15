import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players too get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
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
            # check for a valid value by cast to integer return invalid
            # check if spot is available if not return invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again?')

        return val


class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # randomly choose a square
            square = random.choice(game.available_moves())
        else:
            # choose a square using minimax algorithm
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state, player):
        max_player = self.letter  # human
        # the other player what letter is available
        other_player = 'O' if player == 'X' else 'X'

        # first check if previous move is a winner
        if state.current_winner == other_player:
            # return position and score for minimax algorithm
            return {'postion': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }

        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # initialize dictionaries
        if player == max_player:
            # each score should maximize
            best = {'position': None, 'score': -math.inf}
        else:
            # each score should minimize
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)  # alternate players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # optimal next move

            # step 4: update dictionary
            if player == max_player:  # maximize max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # minimize other_player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best