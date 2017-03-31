n = 87

def palindrome_chain_length(n):
    count = 0
    while n!=int(str(n)[::-1]):
        n = n + int(str(n)[::-1])
        count += 1
    return count

print palindrome_chain_length(n)
