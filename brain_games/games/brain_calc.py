import random
from typing import Tuple


def get_question() -> Tuple[str, str]:
    operand1 = random.randrange(1, 10)
    operand2 = random.randrange(1, 10)

    operations = ['+', '-', '*']

    question = f'{operand1} {operations[random.randrange(0, 3)]} {operand2}'
    answer = eval(question)

    return question, str(answer)
