#!/usr/bin/env python
from brain_games.cli import run_game
from brain_games.games.brain_progression import get_question


def main():
    run_game(
        description='What number is missing in the progression?',
        get_question=get_question,
    )


if __name__ == '__main__':
    main()
