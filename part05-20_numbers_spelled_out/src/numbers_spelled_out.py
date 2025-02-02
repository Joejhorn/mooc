# Write your solution here
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    numbers_dict = {}
    
    for i in range(100):
        if i < 10:
            numbers_dict[i] = ones[i]
        elif i < 20:
            numbers_dict[i] = teens[i - 10]
        else:
            tens_part = tens[i // 10]
            ones_part = "" if i % 10 == 0 else "-" + ones[i % 10]
            numbers_dict[i] = tens_part + ones_part
    
    return numbers_dict

if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
