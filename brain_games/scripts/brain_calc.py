#!/usr/bin/env python
from brain_games.engine import run_game
from brain_games.games.brain_calc import DESCRIPTION, question_maker


def main():
    run_game(
        description=DESCRIPTION,
        question_maker=question_maker,
    )


if __name__ == '__main__':
    main()
