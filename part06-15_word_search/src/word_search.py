from itertools import product

def open_db():
    if not hasattr(open_db, "dic_words"):
        with open('words.txt') as f:
            open_db.dic_words = {word.strip().lower() for word in f} 
    return open_db.dic_words

def is_it_valid(dic_words, new_term):
    return new_term.lower() in dic_words

def find_words(term):
    dic_words = open_db()
    valid_words = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if "." in term:
        indices = [i for i, c in enumerate(term) if c == '.']
        generated_words = set()
        for replacement in product(alphabet, repeat=len(indices)):  
            new_term = list(term)
            for i, char in zip(indices, replacement):  
                new_term[i] = char  
            new_term = "".join(new_term)
            if is_it_valid(dic_words, new_term):  
                generated_words.add(new_term)
        return sorted(list(generated_words)) 

    elif '*' in term:
        if term.startswith('*'):
            suffix = term[1:]
            valid_words = [word for word in dic_words if word.endswith(suffix)]
        elif term.endswith('*'):  
            prefix = term[:-1]
            valid_words = [word for word in dic_words if word.startswith(prefix)]
        return sorted(valid_words)  

    elif is_it_valid(dic_words, term):
        return [term]

    return []  

if __name__ == '__main__':
    pass