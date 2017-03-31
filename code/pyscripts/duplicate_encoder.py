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

print duplicate_encode(word)
