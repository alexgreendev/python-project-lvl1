#!/usr/bin/env python
from brain_games.cli import run_game
from brain_games.games.brain_gcd import get_question


def main():
    run_game(
        description='Find the greatest common divisor of given numbers.',
        get_question=get_question,
    )


if __name__ == '__main__':
    main()
