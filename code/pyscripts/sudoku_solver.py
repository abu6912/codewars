puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
         ]

def all_arrays(puzzle, row, col):
    range_dict = [
                    [0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                 ]
    for key in range_dict:
        if row in key:
            inter1 = puzzle[key[0]:key[-1]+1]
    inter2 = []
    for key in range_dict:
        if col in key:
            for rows in inter1:
                inter2.extend(rows[key[0]:key[-1]+1])
    return puzzle[row], [rows[col] for rows in puzzle], inter2

def sudoku(puzzle):
    #print puzzle
    inter = [[0]*9 for ind in range(9)]
    for row_index, row in enumerate(puzzle):
        #print 'inter: ', inter
        for col_index, item in enumerate(row):
            if item == 0:
                dependent_arrays = all_arrays(puzzle, row_index, col_index)
                exclude_values = set([item for sublist in dependent_arrays for item in sublist])
                exclude_values.discard(0)
                if len(set(range(1, 10)) - exclude_values)==1:
                    inter[row_index][col_index] = list(set(range(1, 10)) - exclude_values)[0]
            else:
                inter[row_index][col_index] = item
    if any(0 in row for row in puzzle):
        inter = sudoku(inter)
    return inter

'''
from itertools import product

def possibles(puzzle, x, y):
    a, b = 3*(x/3), 3*(y/3)
    square = set([puzzle[r][c] for r, c in product(range(a,a + 3), range(b,b + 3))])
    row = set(puzzle[x])
    col = set(zip(*puzzle)[y])
    return set(range(1,10)).difference(square.union(row).union(col))

def sudoku(puzzle):
    z = [(r,c) for (r,c) in product(range(9),range(9)) if puzzle[r][c] == 0]
    if z == []:
        return puzzle
    for (r,c) in z:
        p = possibles(puzzle, r, c)
        if len(p) == 1:
            puzzle[r][c] = p.pop()
    return sudoku(puzzle)
'''

if __name__ == '__main__':
    for line in puzzle:
        print line
    print '--'
    for line in sudoku(puzzle):
        print line


