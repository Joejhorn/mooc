# Write your solution here
def histogram(word):
    hist_dic = {}
    for char in word:
        if char not in hist_dic:
            hist_dic[char] = 1
        else:
            hist_dic[char] += 1
    for k,v in hist_dic.items():
        print(f'{k} {'*' * v}')





if __name__ == '__main__':

    histogram("statistically")