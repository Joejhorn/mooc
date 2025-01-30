# Write your solution here
def length_of_longest(list):
    longest = ""
    for word in list:
        if len(word) > len(longest):
            longest = word
    return len(longest)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
