triplets = [
            ['t','u','p'],
            ['w','h','i'],
            ['t','s','u'],
            ['a','t','s'],
            ['h','a','p'],
            ['t','i','s'],
            ['w','h','s']
           ]

import itertools
def recoverSecret(triplets):
    '''There is a secret string which is unknown to you. Given a collection of 
    random triplets from the string, recover the original string.
    A triplet here is defined as a sequence of three letters such that each letter
    occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

    As a simplification, you may assume that no letter occurs more than once in 
    the secret string.
    You can assume nothing about the triplets given to you other than that they 
    are valid triplets and that they contain sufficient information to deduce the 
    original string. In particular, this means that the secret string will never 
    contain letters that do not occur in one of the triplets given to you.

    secret = "whatisup"
    triplets = [
                ['t','u','p'],
                ['w','h','i'],
                ['t','s','u'],
                ['a','t','s'],
                ['h','a','p'],
                ['t','i','s'],
                ['w','h','s']
               ]
    '''
    all_letters = []
    for trip in triplets:
        all_letters.extend(trip)
    all_letters = list(set(all_letters))
    for subset in itertools.permutations(all_letters, len(all_letters)):
        cond = True
        for trip in triplets:
            cond = cond and subset.index(trip[0]) < subset.index(trip[1]) < subset.index(trip[2])
            if not cond:
                break
        if cond:
            return ''.join(subset)

def firstletter(triplets):
    first_let = []
    for trip in triplets:
        if trip[0] not in first_let:
            first_let.append(trip[0])
    count = 0
    while count<=50 and len(first_let)!=1:
        count +=1
        _dict = {let: first_let.index(let) for let in first_let}
        for trip in triplets:
            occur = [let for let in trip if let in first_let]
            if len(occur)>1:
                first_let = [let for let in first_let if let not in occur[1:]]
    return first_let

if __name__ == '__main__':
    print recoverSecret(triplets)
    print firstletter(triplets)

