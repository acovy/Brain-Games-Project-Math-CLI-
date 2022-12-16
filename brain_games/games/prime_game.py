from random import randint


LOWER_LIMIT = 1
UPPER_LIMIT = 100

DESCRIPTION = 'What number is missing in the progression?'


def prime(random_number):
    for i in range(2, random_number):
        if random_number % i == 0:
            prime = False
            break
    else:
        prime = True
    if random_number == 1:
        prime = False
    return prime


def generate_question_answer():
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'Question: {random_number}' + "\n"
    correct_answer = "yes" if prime(random_number) is True else "no"
    return question, correct_answer
