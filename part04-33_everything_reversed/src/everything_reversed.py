# Write your solution here

def everything_reversed(list):
    new_list = []
    for items in list:
        new_list.append(items[::-1])
    new_list.reverse()
    return new_list
    

if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(['fed', 'cba'])
    print(new_list)