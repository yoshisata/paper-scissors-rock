import unittest

from rules import Choice, RoundResult, determine_winner


class TestRules(unittest.TestCase):

    def test_choice_from_number(self):
        self.assertEqual(Choice.from_number(1), Choice.ROCK)
        self.assertEqual(Choice.from_number(2), Choice.PAPER)
        self.assertEqual(Choice.from_number(3), Choice.SCISSORS)

    def test_determine_winner(self):
        self.assertEqual(determine_winner(Choice.ROCK, Choice.SCISSORS), RoundResult.USER_WIN)
        self.assertEqual(determine_winner(Choice.PAPER, Choice.ROCK), RoundResult.USER_WIN)
        self.assertEqual(determine_winner(Choice.SCISSORS, Choice.PAPER), RoundResult.USER_WIN)
        self.assertEqual(determine_winner(Choice.ROCK, Choice.ROCK), RoundResult.DRAW)


if __name__ == '__main__':
    unittest.main()
