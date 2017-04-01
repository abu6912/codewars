l1= [2, 3, 7, 5]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

import itertools

def Sum_pairs(ints, s):
#    while len(ints)>1:
#        first_num = ints.pop(0)
#        for num in ints:
#            if first_num + num == s:
#                if sum_pairs(ints[:ints.index(num)], s) is not None:
#                    return sum_pairs(ints[:ints.index(num)], s)
#                return [first_num, num]
    if len(ints) <= 0:
        return None
#    all_pairs = []
#    for pair in itertools.combinations(ints, 2):
#        if sum(pair) == s:
#            print(ints[ints.index(pair[0])+1:ints.index(pair[1])])
#            if sum_pairs(ints[ints.index(pair[0])+1:ints.index(pair[1])], s) is not None:
#                return sum_pairs(ints[ints.index(pair[0])+1:ints.index(pair[1])], s)
#            return list(pair)
    
    return None

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
        
if __name__ == '__main__':
    print(sum_pairs(l5, 10))