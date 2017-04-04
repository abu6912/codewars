array = [
            #[1,2,3],
            #[4,5,6],
            #[7,8,9],
            # [1, 2],
            # [3, 4],
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]

def snail(array):
    n = len(array)
    if n == 1:
        return array[0]
    out = []
    left = []
    right = []
    new_arr = []
    for _list in array[1:n-1]:
        right.append(_list[-1])
        left.append(_list[0])
        new_arr.append(_list[1:n-1])
    out.extend(array[0])
    if right:
        out.extend(right)
    out.extend(array[-1][::-1])
    if left:
        out.extend(left[::-1])
    if new_arr:
        out.extend(snail(new_arr))
    return out

'''
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
'''
if __name__ == '__main__':
    print snail(array)
