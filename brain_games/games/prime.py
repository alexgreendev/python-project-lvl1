import random
from typing import Tuple


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question() -> Tuple[str, str]:
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer


def is_prime(num: int):
    if num < 2 or (num > 2 and not num % 2):
        return False
    if num == 2:
        return True
    div = 3
    while div <= num // 2:
        if not num % div:
            return False
        div += 2
    return True
