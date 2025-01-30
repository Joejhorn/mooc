# Write your solution here
def all_the_longest(list):
    results =[]
    longest = max(list, key = len)
    for word in list:
        if len(word) >= len(longest):
            longest = word
            results.append(word)
            
    return results

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']