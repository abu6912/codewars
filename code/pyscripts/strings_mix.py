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

def string_dict(string, count, letter, s):
    if count in string.keys():
        string[count].append(s+':'+count*letter)
    else:
        string[count] = [s+':'+count*letter]
    return string

def mix(s1, s2):
    s1 = sortstring(s1)
    s2 = sortstring(s2)
    all_let = []
    all_let.extend(s1.keys())
    all_let.extend(s2.keys())
    all_let = list(set(all_let))
    all_let.sort()
    string = {}
    for letter in all_let:
        if letter in s1.keys() and letter in s2.keys():
            if s1[letter]==s2[letter]:
                string = string_dict(string, s1[letter], letter, '=')
            elif s1[letter]>s2[letter]:
                string = string_dict(string, s1[letter], letter, '1')
            elif s1[letter]<s2[letter]:
                string = string_dict(string, s2[letter], letter, '2')
        elif letter in s1.keys():
            string = string_dict(string, s1[letter], letter, '1')
        elif letter in s2.keys():
            string = string_dict(string, s2[letter], letter, '2')
    count_keys = string.keys()
    count_keys.sort(reverse = True)
    out = []
    for count in count_keys:
        data = string[count]
        data.sort()
        out.extend(data)
    return '/'.join(out)

if __name__ == '__main__':
    print mix(s1, s2)

    s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
    s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
    print mix(s1, s2)


