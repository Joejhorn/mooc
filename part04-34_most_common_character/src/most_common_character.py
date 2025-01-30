# Write your solution here

def most_common_character(string):
    x = 1
    common = ''
    for char in string:
        if string.count(char) > x:
            common = char
            x += 1
    return common

if __name__ == '__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))