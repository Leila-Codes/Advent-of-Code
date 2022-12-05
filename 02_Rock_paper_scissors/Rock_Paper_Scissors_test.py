import unittest
from Rock_Paper_Scissors import Result, Choice, get_result, choice_from_string, calc_score_from_strategy


class TestRockPaperScissors(unittest.TestCase):
    def test_win_with_eight(self):
        player_choice = Choice.PAPER
        opponent_choice = Choice.ROCK

        result = get_result(player_choice, opponent_choice)

        score = int(player_choice) + int(result)

        self.assertEqual(score, 8)

    def test_lose_with_one(self):
        opponent = choice_from_string('B')
        player = choice_from_string('A')

        result = get_result(player, opponent)

        score = int(result) + int(player)

        self.assertEqual(score, 1)

    def test_round_draw_with_six(self):
        opponent = choice_from_string('Z')
        player = choice_from_string('S')

        result = get_result(player, opponent)

        score = int(result) + int(player)

        self.assertEqual(score, 6)

    def test_score_total(self):
        test_strategy = """A Y
B X
C Z"""

        total_score = calc_score_from_strategy(test_strategy)

        self.assertEqual(total_score, 15)


if __name__ == '__main__':
    unittest.main()
