from enum import Enum
from pathlib import Path
from typing import Tuple, List

puzzle_input = Path('inputs/2').read_text()


def prepare_input_data(input_text: str) -> List[Tuple[str, str]]:
    return [(line.split()[0], line.split()[1]) for line in input_text.splitlines()]


class GameMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class PossibleEndings(Enum):
    LOSE = 'lose'
    DRAW = 'draw'
    WIN = 'win'


opponent_translation = {
    'A': GameMove.ROCK,
    'B': GameMove.PAPER,
    'C': GameMove.SCISSORS
}

player_translation = {
    'X': GameMove.ROCK,
    'Y': GameMove.PAPER,
    'Z': GameMove.SCISSORS
}

endings_translation = {
    'X': PossibleEndings.LOSE,
    'Y': PossibleEndings.DRAW,
    'Z': PossibleEndings.WIN
}


def what_should_player_play(opponent_move: GameMove, how_round_needs_to_end: PossibleEndings) -> GameMove:
    if how_round_needs_to_end == PossibleEndings.DRAW:
        return GameMove(opponent_move.value)
    if how_round_needs_to_end == PossibleEndings.LOSE:
        return what_answer_to_lose(opponent_move)
    return what_answer_to_win(opponent_move)


def calculate_round_score(opponent_move: GameMove, player_move: GameMove):
    score = player_move.value
    if opponent_move.value == player_move.value:
        score = 3 + score
    if does_player_win(opponent_move, player_move):
        score = 6 + score
    return score


def does_player_win(opponent_move: GameMove, player_move: GameMove) -> bool:
    if player_move == GameMove.ROCK and opponent_move == GameMove.SCISSORS:
        return True
    if player_move == GameMove.PAPER and opponent_move == GameMove.ROCK:
        return True
    if player_move == GameMove.SCISSORS and opponent_move == GameMove.PAPER:
        return True
    return False


def what_answer_to_lose(opponent_move: GameMove) -> GameMove:
    if opponent_move == GameMove.SCISSORS:
        return GameMove.PAPER
    if opponent_move == GameMove.ROCK:
        return GameMove.SCISSORS
    if opponent_move == GameMove.PAPER:
        return GameMove.ROCK


def what_answer_to_win(opponent_move: GameMove) -> GameMove:
    if opponent_move == GameMove.SCISSORS:
        return GameMove.ROCK
    if opponent_move == GameMove.ROCK:
        return GameMove.PAPER
    if opponent_move == GameMove.PAPER:
        return GameMove.SCISSORS


input_data = prepare_input_data(puzzle_input)
# 2.1
game_moves = [(opponent_translation[data[0]], player_translation[data[1]]) for data in input_data]
print(sum([calculate_round_score(game_round[0], game_round[1]) for game_round in game_moves]))

# 2.2
game_strategies = [(opponent_translation[data[0]], endings_translation[data[1]]) for data in input_data]
total_game_score = 0
for game_strategy in game_strategies:
    opponent_move = game_strategy[0]
    player_move = what_should_player_play(opponent_move, game_strategy[1])
    round_score = calculate_round_score(opponent_move, player_move)
    total_game_score += round_score
print(total_game_score)
