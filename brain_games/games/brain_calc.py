import random
from typing import Tuple

DESCRIPTION = 'What is the result of the expression?'


def question_maker() -> Tuple[str, str]:
    operand1 = random.randrange(1, 10)
    operand2 = random.randrange(1, 10)

    operations = ['+', '-', '*']

    question = f'{operand1} {operations[random.randrange(0, 3)]} {operand2}'
    answer = eval(question)

    return question, str(answer)
