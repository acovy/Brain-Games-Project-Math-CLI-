from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


LOWER_LIMIT = 1
UPPER_LIMIT = 100


def generate_numbers():
    num_1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    return num_1, num_2


def gcd_calc(num_1, num_2):
    if num_1 == 0:
        correct_answer = 0
    if num_1 == 1 or num_2 == 1:
        correct_answer = 1
    if num_1 > num_2:
        num = num_1
    else:
        num = num_2
    correct_answer = 1
    for i in range(1, num):
        if num_2 % i == 0 and num_1 % i == 0:
            correct_answer = i
    return str(correct_answer)


def generate_question_answer():
    num_1, num_2 = generate_numbers()
    question = f'Question: {num_1} {num_2}' + "\n"
    correct_answer = gcd_calc(num_1, num_2)
    return question, str(correct_answer)
