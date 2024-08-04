from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from functools import lru_cache

ChoiceValue = namedtuple('ChoiceValue', ['number', 'emoji'])


class Choice(Enum):
    ROCK = ChoiceValue(1, '✊')
    PAPER = ChoiceValue(2, '✋')
    SCISSORS = ChoiceValue(3, '✌️')

    def __str__(self) -> str:
        return f'{self.name.capitalize()} {self.value.emoji}'

    @classmethod
    def _initialize_map(cls) -> None:
        """Initialize the mapping of numbers to Choice enums."""

        if not hasattr(cls, '_number_to_choice_map'):
            cls._number_to_choice_map = {choice.value.number: choice for choice in cls}

    @classmethod
    @lru_cache(None)
    def from_number(cls, number: int) -> 'Choice':
        """Convert a number to a Choice enum using a precomputed map and caching."""

        cls._initialize_map()

        if number in cls._number_to_choice_map:
            return cls._number_to_choice_map[number]

        else:
            raise ValueError(f'Invalid choice number: {number}')


class RoundResult(Enum):
    DRAW = 'Draw!'
    USER_WIN = 'You win!'
    COMPUTER_WIN = 'Computer wins!'


@dataclass
class RoundInfo:
    user_choice: Choice
    computer_choice: Choice
    result: RoundResult


WINNING_CONDITIONS = {
    Choice.ROCK: [Choice.SCISSORS],
    Choice.PAPER: [Choice.ROCK],
    Choice.SCISSORS: [Choice.PAPER],
}


def determine_winner(user_choice: Choice, computer_choice: Choice) -> RoundResult:
    """Determine the winner of a round."""

    if user_choice == computer_choice:
        return RoundResult.DRAW

    elif computer_choice in WINNING_CONDITIONS[user_choice]:
        return RoundResult.USER_WIN

    else:
        return RoundResult.COMPUTER_WIN
