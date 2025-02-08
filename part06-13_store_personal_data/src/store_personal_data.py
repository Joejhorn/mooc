# Write your solution here

def store_personal_data(person: tuple):
    line_to_write = ''

    for x, data in enumerate(person):
        line_to_write += str(person[x]) + ';'
    line_to_write = line_to_write[:-1]
    with open('people.csv', 'a') as f:
        f.write(line_to_write + '\n')




if __name__ == '__main__':  
    store_personal_data(("Paul Paulson", 37, 175.5, 24))






# Timothy Test;45;160.0