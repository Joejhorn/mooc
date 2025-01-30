# Write your solution here
def sum_of_positives(list):
    total = 0
    for num in list:
        if num > 0:
            total += num
    return total


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)