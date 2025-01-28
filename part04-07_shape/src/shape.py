def line(num, text):
    if not text:
        text = "*"
    print(text[0] * num)

def shape(size, character, size1, character1):
    # You should call function line here with proper parameters
    for i in range(size):
        line(i+1, character)
    for i in range(size1):
        line(size, character1)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(2, "o", 4, "+")