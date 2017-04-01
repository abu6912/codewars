string = "(){}"

def validBraces(string):
    brace_dict = {
                    '(': ')',
                    '{': '}',
                    '[': ']',
                 }
    if len(string)==0:
        return True
    brace_open = string[0]
    if brace_open not in brace_dict.keys():
        return False
    brace_close = brace_dict[brace_open]
    close_loc = string.find(brace_close)
    if close_loc == -1:
        return False
    brace_string = string[1:close_loc]
    count_brace_open = list(brace_string).count(brace_open)
    if count_brace_open>0:
        dummy = string.replace(brace_close, '|', count_brace_open)
        close_loc = dummy.find(brace_close)
        brace_string = string[1:close_loc]
    if len(brace_string)==0:
        out = True
    else:
        out = validBraces(brace_string)
    if not out:
        return False
    rem_string = string[close_loc+1:]
    return validBraces(rem_string)
    
    
if __name__ == '__main__':
    print(validBraces(string))