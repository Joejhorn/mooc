# Write your solution here
def invert(dictionary):
    delete_list = []
    for key, value in dictionary.items():
        delete_list.append((key, value))
    for data in delete_list:
        del dictionary[data[0]]
        dictionary[data[1]] = data[0]
        
    
if __name__ == '__main__':

    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)