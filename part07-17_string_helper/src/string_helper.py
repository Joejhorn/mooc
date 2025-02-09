# Write your solution here
import string

def change_case(orig_string):
    new_string = ""
    for char in orig_string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            if char == ' ':
                new_string += char.lower()  
    return new_string

def split_in_half(orig_string):
    split_point = int(len(orig_string) / 2)
    return (orig_string[0:split_point], orig_string[split_point:])

def remove_special_characters(orig_string):
    allowed_chars = string.ascii_letters + '0123456789' + ' '
    new_string = ""
    for char in orig_string:
        if char not in allowed_chars:
            continue
        else:
            new_string += char
    return new_string

if __name__ == '__main__':
    print(change_case('two different words'))
    print(remove_special_characters("Thi§ is a test test"))