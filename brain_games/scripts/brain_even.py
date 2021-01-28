#!/usr/bin/env python
from brain_games.cli import run_game
from brain_games.games.brain_even import get_question


def main():
    run_game(
        description='Answer "yes" if the number is even,'
                    ' otherwise answer "no".',
        get_question=get_question,
    )


if __name__ == '__main__':
    main()
