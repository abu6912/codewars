walk = ['n', 'n', 'n', 'n', 'n',
        's', 's', 's', 's', 's']
def isValidWalk(walk):
    if len(walk)==10:
        xaxis = sum('n'==letter for letter in walk) - sum('s'==letter for letter in walk)
        yaxis = sum('e'==letter for letter in walk) - sum('w'==letter for letter in walk)
        return xaxis==0 and yaxis==0
    return False
print isValidWalk(walk)
