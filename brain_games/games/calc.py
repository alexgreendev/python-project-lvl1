import random
from typing import Tuple


def get_description():
    return 'What is the result of the expression?'


def make_question() -> Tuple[str, str]:
    operand1 = random.randrange(1, 10)
    operand2 = random.randrange(1, 10)

    operations = ['+', '-', '*']
    operation_index = random.randrange(0, len(operations))

    question = f'{operand1} {operations[operation_index]} {operand2}'
    answer = eval(question)

    return question, str(answer)
