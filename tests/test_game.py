import unittest
from unittest.mock import patch

from game import PaperScissorsRockGame
from rules import Choice, RoundResult


class TestPaperScissorsRockGame(unittest.TestCase):

    def test_get_computer_choice(self):
        choice = PaperScissorsRockGame.get_computer_choice()
        self.assertIn(choice, Choice)

    @patch('builtins.input', side_effect=[1, 2, 3])
    def test_get_user_choice(self, mock_input):
        game = PaperScissorsRockGame(1)
        self.assertEqual(game.get_user_choice(), Choice.ROCK)
        self.assertEqual(game.get_user_choice(), Choice.PAPER)
        self.assertEqual(game.get_user_choice(), Choice.SCISSORS)

    @patch('builtins.input', side_effect=[1])
    def test_play_round(self, mock_input):
        game = PaperScissorsRockGame(1)
        with patch.object(game, 'get_computer_choice', return_value=Choice.ROCK):
            game.play_round()
            self.assertEqual(len(game.rounds), 1)
            self.assertEqual(game.rounds[0].user_choice, Choice.ROCK)
            self.assertEqual(game.rounds[0].computer_choice, Choice.ROCK)
            self.assertEqual(game.rounds[0].result, RoundResult.DRAW)

    @patch('builtins.input', side_effect=['1'])
    def test_get_number_of_rounds(self, mock_input):
        self.assertEqual(PaperScissorsRockGame.get_number_of_rounds(), 1)

    @patch('builtins.input', side_effect=['11', 'y'])
    def test_get_number_of_rounds_confirm(self, mock_input):
        self.assertEqual(PaperScissorsRockGame.get_number_of_rounds(), 11)

    @patch('builtins.input', side_effect=['11', 'n', '5'])
    def test_get_number_of_rounds_reject(self, mock_input):
        self.assertEqual(PaperScissorsRockGame.get_number_of_rounds(), 5)

    @patch('builtins.input', side_effect=['invalid', '5'])
    def test_get_number_of_rounds_invalid_input(self, mock_input):
        self.assertEqual(PaperScissorsRockGame.get_number_of_rounds(), 5)


if __name__ == '__main__':
    unittest.main()
