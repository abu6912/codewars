l1= [2, 3, 7, 5]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

def sum_pairs(ints, s):
    while len(ints)>1:
        first_num = ints.pop(0)
        for num in ints:
            if first_num + num == s:
                return [first_num, num]
    pass

if __name__ == '__main__':
    print(sum_pairs(l1, 10))