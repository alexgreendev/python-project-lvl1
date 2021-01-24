import prompt


def welcome_user():
    name = prompt.string(prompt="May I have your name? ")
    print(f'Hello, {name}!')
