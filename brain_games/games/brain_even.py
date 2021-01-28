import random
from typing import Tuple


def get_question() -> Tuple[str, str]:
    rand_num = random.randrange(1, 100)
    answer = 'no' if rand_num % 2 else 'yes'
    return str(rand_num), answer
