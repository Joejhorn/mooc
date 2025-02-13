
def balanced_brackets(my_string: str):
    my_string = ''.join([character for character in my_string if character in '()[]'])
    print(my_string)
    if len(my_string) == 0:
        return True

    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)

    ok = balanced_brackets("()())")
    print(ok)

    ok = balanced_brackets(")()")
    print(ok)

    ok = balanced_brackets("()(())")
    print(ok)

