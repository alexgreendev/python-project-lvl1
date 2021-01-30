from typing import Callable

import prompt

from brain_games.cli import welcome_user

GAME_ROUNDS = 3


def run_game(
    description: str,
    question_maker: Callable,
):
    user_name = welcome_user()
    print(description)

    for step in range(0, GAME_ROUNDS):
        question, correct_answer = question_maker()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
