# Write your solution here
def remove_smallest(list):
    x = min(list)
    list.remove(x)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)