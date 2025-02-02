# Write your solution here
def times_ten(x,y):
    ten = {}
    for i in range(x,y+1):
        ten[i] = i*10     
    return ten   

if __name__ == '__main__':
    d = times_ten(3, 6)
    print(d)