text = 'Pig latin is cool'

def pig_it(text):
    text = text.split(' ')
    out = ''
    for word in text:
        if word.isalpha():
            init = word[0]
            rest = word[1:]
            out += ' {0}{1}ay'.format(rest, init)
        else:
            out += ' ' + word
    return out.strip()
print pig_it(text)
