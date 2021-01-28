from typing import Callable

import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def run_game(
    description: str,
    get_question: Callable,
):
    user_name = welcome_user()
    print(description)

    for step in range(0, 3):
        question, correct_answer = get_question()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
