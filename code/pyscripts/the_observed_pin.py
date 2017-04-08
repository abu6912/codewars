expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

import itertools

num_dict = {
            '1': ('1', '2', '4'),
            '2': ('1', '2', '3', '5'),
            '3': ('2', '3', '6'),
            '4': ('1', '4', '5', '7'),
            '5': ('2', '4', '5', '6', '8'),
            '6': ('3', '5', '6', '9'),
            '7': ('4', '7', '8'),
            '8': ('5', '7', '8', '9', '0'),
            '9': ('6', '8', '9'),
            '0': ('8', '0')
           }
           
def get_pins(observed):
    '''TODO: This is your job, detective!'''
    combos = [num_dict[num] for num in observed]
    return [ ''.join(num_list) for num_list in list(itertools.product(*combos))]

'''
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
'''

if __name__ == '__main__':
    for tup in expectations:
        print(get_pins(tup[0]))