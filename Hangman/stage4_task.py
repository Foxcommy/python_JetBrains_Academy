import random

welcome_msg = 'H A N G M A N'
values = ['python', 'java', 'swift', 'javascript']
answer = random.choice(values)
n_guess_letters = 3
len_dash = len(answer) - n_guess_letters
user_answer = input('Guess the word: ' + answer[:n_guess_letters] + '-' * len_dash)

if user_answer == answer:
    print('You survived!')
else:
    print('You lost!')
