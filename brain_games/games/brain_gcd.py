import random
from typing import Tuple


def get_question() -> Tuple[str, str]:
    num1 = random.randrange(20, 100)
    num2 = random.randrange(20, 100)

    question = f'{num1} {num2}'
    answer = greatest_common_divisor(num1, num2)

    return question, str(answer)


def greatest_common_divisor(
    num1: int,
    num2: int,
) -> int:
    if not num2:
        return num1
    return greatest_common_divisor(num2, num1 % num2)
