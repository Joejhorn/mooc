# Write your solution here
def factorials(number):
    factorial_dict = {}
    fact = 1  
    for i in range(1, number + 1):
        fact *= i  
        factorial_dict[i] = fact  
    return factorial_dict

        
        
if __name__ == '__main__':

    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])