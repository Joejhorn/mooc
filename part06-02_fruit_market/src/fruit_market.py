# write your solution here
import os



def read_fruits():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "fruits.csv")

    fruit_dic = {}
    with open(file_path) as fruits:
        for fruit in fruits:
            data = fruit.split(';')
            fruit_dic[data[0]] = float(data[1])
    return fruit_dic

if __name__ == "__main__":
    print(read_fruits())

