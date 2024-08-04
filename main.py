import logging
import sys

from game import PaperScissorsRockGame

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)],
)


if __name__ == '__main__':
    """Entry point of the application."""

    try:
        number_of_rounds = PaperScissorsRockGame.get_number_of_rounds()
        game = PaperScissorsRockGame(number_of_rounds)
        game.play_game()

    except ValueError:
        logging.error('Please enter a valid number of rounds.')
