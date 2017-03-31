seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
def find_it(seq):
    uniq_seq = list(set(seq))
    appears = []
    for num in uniq_seq:
        appears.append(sum(num==seq_num for seq_num in seq))
        appears = [app%2 for app in appears]
    return uniq_seq[appears.index(max(appears))]

print find_it(seq)
