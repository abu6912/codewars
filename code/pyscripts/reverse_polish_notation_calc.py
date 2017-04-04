expr = '1 2 3.5'
# (which is equivalent to 5 + ((1 + 2) * 4) - 3

def checkvalid(string):
    if string in ['+', '-', '*', '/']:
        return True
    try:
        val = float(string)
        return True
    except ValueError:
        return False

def checkFloat(expr):
    print expr
    return any(not element==int(float(element)) for element in expr if element not in ('+', '-', '*', '/'))

def findOperator(expr):
    operators = ('+', '-', '*', '/')
    location = [expr.index(opr) for opr in operators if opr in expr]
    if location:
        return min(location)
    else:
        return -1

def performOperatior(expr):
    num1 = float(expr[0])
    num2 = float(expr[1])
    operator = expr[2]
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

def replaceContent(expr, operator_loc):
    inter = expr[operator_loc-2:operator_loc+1]
    op_out = performOperatior(inter)
    expr = expr[:operator_loc-2] + [op_out] + expr[operator_loc+1:]
    return expr

def calc(expr):
    expr = expr.split(' ')
    if any(not checkvalid(string) for string in expr):
        return False
    floatpresent = checkFloat(expr)
    print floatpresent

    operators = ('+', '-', '*', '/')
    if not expr:
        return 0
    if findOperator(expr) == -1:
        return float(expr[-1]) if floatpresent else int(expr[-1])
    elif findOperator(expr) > 1:
        expr= replaceContent(expr, findOperator(expr))
        if len(expr)>2:
            expr = [str(element) for element in expr]
            return calc(' '.join(expr))
        return float(expr[0]) if floatpresent else int(expr[0])

'''
import operator

def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()
'''

if __name__ == '__main__':
    print calc(expr)
