# write your solution here
with open('wordlist.txt') as f:
    dic_words = []
    for word in f:
        dic_words.append(word.strip().lower())

sentence = input('Write Text: ')
word = sentence.split()
new_sentence = ""
for w in word:
    if w.lower() not in dic_words:
        new_sentence += f'*{w}* '
    else:
        new_sentence += f'{w} '

print(new_sentence)




