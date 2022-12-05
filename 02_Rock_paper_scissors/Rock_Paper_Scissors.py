from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        if self == Choice.ROCK:
            return "ROCK"
        elif self == Choice.PAPER:
            return "PAPER"
        elif self == Choice.SCISSORS:
            return "SCISSORS"

        return "INVALID"

    def __int__(self):
        return self.value


def choice_from_string(raw_choice: str) -> Choice:
    if raw_choice in ['A', 'X']:
        return Choice.ROCK
    elif raw_choice in ['B', 'Y']:
        return Choice.PAPER
    elif raw_choice in ['C', 'Z']:
        return Choice.SCISSORS
    else:
        raise ValueError("Choice must be one of (A, B, C) for the player and (X, Y, Z) for the opponent.")


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    def __str__(self):
        if self == Result.WIN:
            return "WIN"
        elif self == Result.DRAW:
            return "DRAW"
        elif self == Result.LOSS:
            return "LOSS"
        return "INVALID"

    def __int__(self):
        return self.value


# ROCK -> SCISSORS
# PAPER -> ROCK
# SCISSORS -> PAPER
def get_result(player: Choice, opponent: Choice) -> Result:
    if player == opponent:
        return Result.DRAW

    if (player == Choice.ROCK and opponent == Choice.SCISSORS) \
            or (player == Choice.PAPER and opponent == Choice.ROCK) \
            or (player == Choice.SCISSORS and opponent == Choice.PAPER):
        return Result.WIN

    return Result.LOSS


def calc_score_from_strategy(strategy: str) -> int:
    total_score = 0

    for game in strategy.split('\n'):
        if len(game) < 1:
            continue
        print(f"processing round ({game})")
        [raw_opponent, raw_player] = game.strip().split(' ')
        [player, opponent] = [
            choice_from_string(raw_player),
            choice_from_string(raw_opponent)
        ]

        result = get_result(player, opponent)

        total_score += int(player) + int(result)

    return total_score


def main():
    with open("input.txt", "r") as strategy_guide:
        data = strategy_guide.read()
        final_score = calc_score_from_strategy(data)
        print(f"Final Score is: {final_score}")


if __name__ == "__main__":
    main()
