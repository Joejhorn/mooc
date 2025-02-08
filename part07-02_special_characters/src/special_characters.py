# Write your solution here
import string

def separate_characters(my_string: str):
    asc_char = ''
    punch_char = ''
    other = ''
    for char in my_string:
        if char.lower() in string.ascii_letters.lower():
            asc_char += char
        elif char in string.punctuation:
            punch_char += char
        else:
            other += char

    return (asc_char, punch_char, other)


if __name__ == '__main__':
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
