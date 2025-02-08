# Write your solution here
def read_input(message, low, high):
    while True:
        try:
            results = int(input(message))
            if results > low and results < high:
                return results
        except ValueError:
            pass
        print(f'You must type in an integer between {low} and {high}')

if __name__ == '__main__':
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number)


