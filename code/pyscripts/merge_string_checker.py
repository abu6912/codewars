s = 'Bananas from Bahamas'
part2 = 'Bahas'
part1 = 'Bananas from am'

# s = 'Bahamas'
# part2 = 'Bahas'
# part1 = 'am'
s = 'codewars'
part2 = 'code'
part1 = 'wars'

def is_merge(s, part1, part2):
    #print s, part1, part2
    s = [letter for letter in s]
    part1 = [letter for letter in part1]
    part2 = [letter for letter in part2]
    if len(s) != len(part1) + len(part2):
        return False
    if s and part1 and part2 and part1[0] == s[0] and part2[0] == s[0]:
        if is_merge(''.join(s[1:]), ''.join(part1[1:]), ''.join(part2)) or is_merge(''.join(s[1:]), ''.join(part1), ''.join(part2[1:])):
            return True
    if s and part1 and part1[0] == s[0]:
        s.remove(s[0])
        part1.remove(part1[0])
        return is_merge(''.join(s), ''.join(part1), ''.join(part2))
    if s and part2 and part2[0] == s[0]:
        s.remove(s[0])
        part2.remove(part2[0])
        return is_merge(''.join(s), ''.join(part1), ''.join(part2))

    if not s and not part1 and not part2:
        return True
    return False

if __name__ == '__main__':
    print is_merge(s, part1, part2)
