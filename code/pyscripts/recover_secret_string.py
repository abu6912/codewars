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
def RecoverSecret(triplets):
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
            break
    return ''.join(subset)

def checkpos(arrange, triplets):
    cond = True
    for trip in triplets:
        cond = cond and arrange.index(trip[0]) < arrange.index(trip[1]) < arrange.index(trip[2])
        if not cond:
            break
    return cond

def recoverSecret(triplets):
    all_letters = []
    for trip in triplets:
        all_letters.extend(trip)
    all_letters = list(set(all_letters))
    arrange = ['_' for number in xrange(len(all_letters))]
    for trip in triplets:
        present = sum(letter in arrange for letter in trip)
        if present==0:
            start = arrange.index('_')
            arrange[start] = trip[0]
            arrange[start+1] = trip[0+1]
            arrange[start+2] = trip[0+2]
        elif present==2:
            pass
    return arrange

print recoverSecret(triplets)
