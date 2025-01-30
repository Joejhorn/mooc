# Write your solution here
def list_sum(l1, l2):
    new_list = []
    for x, i in enumerate(l1):
        new_list.append(i + l2[x])
    return new_list

if __name__ == '__main__':
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))    
