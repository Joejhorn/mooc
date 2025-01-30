# Write your solution here
def anagrams(st1, st2):
    if len(st1) != len(st2):
        return False
    list = st1.split()
    for x in st2:
        if x not in st1:
            return False
    return True


if __name__ == "__main__":
    print(anagrams('cat', 'act'))