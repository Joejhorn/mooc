# Write your solution here
def does_it_add(first, symbol, second, answer):

    if symbol == '+':
        return(int(first) + int(second) == int(answer))
    if symbol == '-':
        return( int(first) - int(second) == int(answer))

def filter_solutions():
    signs = ['+', '-']
    first_last = 'first'
    with open('solutions.csv') as f:
        with open('correct.csv', 'w') as c:
            with open('incorrect.csv', 'w') as i:
                for line in f:
                    all = line.strip().split(';')
                    math = all[1]
                    answer = all[2]
                    first = ''
                    second = ''
                    for char in math:
                        if char not in signs and first_last == 'first':
                            first += char
                        elif char not in signs and first_last == 'second':
                            second += char
                        else:
                            symbol = char
                            first_last = "second"
                    first_last = 'first'
                    if does_it_add(first, symbol, second, answer):
                        c.write(line)
                    else:
                        i.write(line)
if __name__ == '__main__':
    filter_solutions()
