# Write your solution here
def create_tuple(x,y,z):
    temp_tup = (x,y,z)
    temp_list = list(temp_tup)
    
    new_tup = (min(temp_list), max(temp_list), sum(temp_list))
    return new_tup

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))