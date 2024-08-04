import logging
import random

from rules import Choice, RoundResult, RoundInfo, determine_winner


class PaperScissorsRockGame:
    MAX_ROUNDS = 10

    def __init__(self, number_of_rounds: int):
        self.number_of_rounds = number_of_rounds
        self.rounds = []
        self.user_score = 0
        self.computer_score = 0

    @staticmethod
    def get_computer_choice() -> Choice:
        """Get a random choice for the computer."""

        return random.choice(list(Choice))

    @staticmethod
    def get_user_choice() -> Choice:
        """Get the user's choice from input."""

        while True:
            try:
                user_input = int(input(
                    f'Enter your choice ('
                    f'1 - {Choice.ROCK}, '
                    f'2 - {Choice.PAPER}, '
                    f'3 - {Choice.SCISSORS}): '))

                return Choice.from_number(user_input)

            except (ValueError, KeyError):
                logging.warning('Invalid choice. Please enter a number between 1 and 3.')

    def play_round(self) -> None:
        """Play a single round of the game."""

        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        self.rounds.append(RoundInfo(user_choice, computer_choice, result))

        logging.info(f'You chose: {user_choice}')
        logging.info(f'Computer chose: {computer_choice}')
        logging.info(result.value)

        if result == RoundResult.USER_WIN:
            self.user_score += 1

        elif result == RoundResult.COMPUTER_WIN:
            self.computer_score += 1

    def play_game(self) -> None:
        """Play the game for the specified number of rounds."""

        for _ in range(self.number_of_rounds):
            self.play_round()

        self.display_results()

    def display_results(self) -> None:
        """Display the results of all rounds and the final score."""

        logging.info('Game Summary:')
        for i, result in enumerate(self.rounds, 1):
            logging.info(
                f'Round {i}: '
                f'You chose {result.user_choice}, '
                f'Computer chose {result.computer_choice} - {result.result.value}',
            )

        logging.info(f'Final Score: You {self.user_score} - {self.computer_score} Computer')

    @classmethod
    def get_number_of_rounds(cls) -> int:
        """Prompt the user to enter the number of rounds and confirms if the input is greater than MAX_ROUNDS amount."""

        while True:
            try:
                rounds = int(input('Enter the number of rounds: '))

                if rounds > cls.MAX_ROUNDS:
                    confirm = input(
                        f'You entered more than {cls.MAX_ROUNDS} rounds. '
                        f'Do you confirm? (Y - Yes, Any other key to start again): ',
                    ).strip().lower()

                    if confirm == 'y':
                        return rounds

                else:
                    return rounds

            except ValueError:
                logging.warning("Invalid input. Please enter a valid number.")
