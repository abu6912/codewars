word = 'recede'

def duplicate_encode(word):
    word = word.lower()
    out = ''
    for letter in word:
        if word.count(letter)>1:
            out += ')'
        else:
            out += '('
    return out

if __name__ == '__main__':
    print duplicate_encode(word)
