# Write your solution here
import difflib
with open('wordlist.txt') as f:
    dic_words = []
    for word in f:
        dic_words.append(word.strip().lower())

sentence = input('write text: ')
word = sentence.split()
new_sentence = ""
mispelled_words = []
for w in word:
    if w.lower() not in dic_words:
        new_sentence += f'*{w}* '
        mispelled_words.append(w)
    else:
        new_sentence += f'{w} '
print(new_sentence)

print('suggestions: ')
for word in mispelled_words:
    possible_matches = difflib.get_close_matches(word, dic_words)
    print(f'{word}: {", ".join(possible_matches)}')
  