bracket_str = '([{hello]})'

open_brackets = ['(','[','{']
close_brackets = [')',']','}']


def match_bracket(brck_str):
    bracket_stack = []
    for char in brck_str:
        if char in open_brackets:
            bracket_stack.append(char)
        elif char in close_brackets:
            pos = close_brackets.index(char)
            if len(bracket_stack) > 0 and (open_brackets[pos] == bracket_stack[len(bracket_stack)-1]):
                bracket_stack.pop()
            else:
                print("Unbalanced")
                break

    if len(bracket_stack) == 0:
        print('Brackets match')
    else:
        print('Brackets do not match')


match_bracket(bracket_str)
