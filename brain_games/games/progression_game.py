from random import randint


DESCRIPTION = 'What number is missing in the progression?'

def generate_question_answer():
    start_digit = randint(1, 15)
    count_digits = randint(5, 10)
    progression = [(i * start_digit) for i in range(1, 11)]
    correct_answer = progression[count_digits]
    progression[count_digits] = '..'
    progression = [str(k) for k in progression]
    progression = " ".join(progression)
    question = f'Question: {progression}' + "\n"
    return question, str(correct_answer)
