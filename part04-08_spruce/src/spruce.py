# Write your solution here


def spruce(size):
    print('a spruce!')
    for i in range(1, size+1):
        spaces = size - i
        char = (2 * i) - 1
        string = " " * spaces  + '*' * char + spaces * " "
        print(string)
        if i == 1:
            last = string
    print(last)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)