# Write your solution here
def palindromes(st1): 
    st2 = st1
    st1 = st1[::-1]
    if st1 == st2:
        return True
    return False

# Note, that at this time the main program should not be written inside
while True:

    word = input('Please type in a palindrome: ')
    if palindromes(word):
        print(f'{word} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")

