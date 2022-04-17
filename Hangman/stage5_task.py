import random

welcome_msg = 'H A N G M A N'
values = ['python', 'java', 'swift', 'javascript']
attempts = 8
answer = random.choice(values)
len_answer = len(answer)
list_answer = list(answer)
set_answer = set(answer)
hint = len_answer * '-'
list_hint = list(hint)
game = 0

print(welcome_msg)
print()


def find_letter(answer, user_letter):
    ix = 0
    ix_search = []
    while ix <= len(answer) - 1:
        if list(answer)[ix] == user_letter:
            ix_search.append(ix)
        ix += 1
    return ix_search


def replacer(to_replace, hint, user_letter):
    list_hint = list(hint)
    for i in to_replace:
        list_hint[i] = user_letter
        new_hint = ''.join(list_hint)
    return new_hint


while game < attempts:
    print(hint)
    user_letter = input('Input a letter: ')
    if user_letter not in set_answer:
        print("That letter doesn't appear in the word.")
        print()
    else:
        to_replace = find_letter(answer, user_letter)
        hint = replacer(to_replace, hint, user_letter)
        print()
    game += 1
    if game == attempts:
        print('Thanks for playing!')
