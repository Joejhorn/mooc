# Write your solution here
def shortest(list):
    shortest = list[0]
    for word in list:
        if len(word) < len(shortest):
            shortest = word
    return shortest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
