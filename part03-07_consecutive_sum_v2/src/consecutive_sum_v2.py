# Write your solution here
limit = int(input("limit: "))
result = 1
counter = 2
string = f"The consecutive sum: 1 + "
while result < limit:


    result += counter
    string += f"{counter} + "
    counter += 1

string = string[:-2]
string += f"= {result}"
print(string)