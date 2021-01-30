import random
from typing import Tuple

DESCRIPTION = 'What number is missing in the progression?'


def question_maker() -> Tuple[str, str]:
    start = random.randint(1, 50)
    step = random.randint(1, 20)
    length = 10

    progression = list(range(start, (start + length * step), step))

    hide_index = random.randrange(0, length)
    answer = progression.pop(hide_index)
    progression.insert(hide_index, '..')

    return ' '.join(map(str, progression)), str(answer)
