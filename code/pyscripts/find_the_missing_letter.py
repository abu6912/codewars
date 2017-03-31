chars = ['a','b','c','d','f']

def find_missing_letter(chars):
    letter_list = [chr(i) for i in xrange(127)][65:91]
    if not any(letter in letter_list for letter in chars):
        letter_list = [letter.lower() for letter in letter_list]
    first = True
    for letter in chars:
        if first:
            index = letter_list.index(letter)
            first = False
        else:
            if letter != letter_list[index]:
                return letter_list[index]
        index += 1

print find_missing_letter(chars)
