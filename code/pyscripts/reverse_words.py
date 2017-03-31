str = 'This  is   an example!'

def reverse_words(str):
    word_list = []
    nstr = str.split(' ')
    word_list = [word[::-1] for word in nstr]
    return ' '.join(word_list)

print str
print reverse_words(str)
