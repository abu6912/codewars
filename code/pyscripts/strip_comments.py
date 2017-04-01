string = "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ["#", "!"]

def solution(string,markers):
    out = []
    for line in string.split('\n'):
        for mrk in markers:
            line = line.split(mrk)[0]
        line = line.strip(' ')
        out.append(line)
    return '\n'.join(out)
        
        
if __name__ == '__main__':
    print(solution(string,markers))