s1 = 'A aaaa bb c'
s2 = '& aaa bbb c d'

def islowerletter(char):
    return char in [chr(i).lower() for i in xrange(127)][65:91]

def sortstring(string):
    letter_list = [letter for letter in string if islowerletter(letter)]
    letter_list.sort()
    letter_dict = {}
    for letter in list(set(letter_list)):
        if letter_list.count(letter)>1:
            letter_dict[letter] = letter_list.count(letter)
    return letter_dict

def mix(s1, s2):
    s1 = sortstring(s1)
    s2 = sortstring(s2)
    all_let = []
    all_let.extend(s1.keys())
    all_let.extend(s2.keys())
    all_let = list(set(all_let))
    all_let.sort()
    string = []
    for letter in all_let:
        if letter in s1.keys() and letter in s2.keys():
            if s1[letter] == s2[letter]:
                string.append('=:'+ s1[letter]*letter)
            elif s1[letter] > s2[letter]:
                string.append('1:'+ s1[letter]*letter)
            elif s1[letter] < s2[letter]:
                string.append('2:'+ s2[letter]*letter)
        else:
            if letter in s1.keys():
                string.append('1:'+ s1[letter]*letter)
            elif letter in s2.keys():
                string.append('2:'+ s2[letter]*letter)
    # string.sort()
    let_dict = {}
    for letter in all_let:
        if s1[letter] == s2[letter]:
            let_dict[letter] = ['=:', s1[letter]]
        elif s1[letter] < s2[letter]:
            let_dict[letter] = ['2:', s2[letter]]
        elif s1[letter] > s2[letter]:
            let_dict[letter] = ['1:', s1[letter]]

    str_len = [len(_str) for _str in string]
    
    return string

if __name__ == '__main__':
    print mix(s1, s2)
