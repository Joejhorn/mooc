# Write your solution here
def new_person(name, age):

    if name == '' or len(name) > 40:
        raise ValueError
    elif age < 1 or age > 150:
        raise ValueError
    else:
        names = name.split(' ')
        print(len(names))
        if len(names) < 2:
            raise ValueError
    return(name, age)

if __name__ == "__main__":
    new_person('andrew', 32)