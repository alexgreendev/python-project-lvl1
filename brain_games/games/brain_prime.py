import random
from typing import Tuple


def get_question() -> Tuple[str, str]:
    num = random.randint(1, 100)
    answer = 'yes' if is_prime(num) else 'no'
    return str(num), answer


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
