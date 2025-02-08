# Write your solution here
from datetime import datetime

def is_it_valid(pic):
    remainders = list('0123456789ABCDEFHJKLMNPRSTUVWXY')
    if len(pic) != 11:
        return False        
    century_marker = pic[6]
    identifer = pic[7:10]
    all_numbers = int((pic[0:6] + identifer))
    control_char = pic[10]
    
    match century_marker:
        case '+':
            century = '18'
        case '-':
            century = '19'
        case 'A':
            century = '20'
    
    try:
        datetime( int(century + pic[4:6]), int(pic[2:4]), int(pic[0:2]))
    except ValueError:
        return False

    return remainders[all_numbers % 31] == control_char

if __name__ == '__main__':
    print(is_it_valid('230827A906F'))