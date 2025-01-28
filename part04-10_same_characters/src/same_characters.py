# Write your solution here
def same_chars(string, pos1, pos2):
    if pos1 > len(string) or pos2  > len(string) - 1:
        return False
    return string[pos1] == string[pos2]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))