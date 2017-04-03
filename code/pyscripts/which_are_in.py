a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    out_list = []
    for word1 in array1:
        for word2 in array2:
            if word2.find(word1) >= 0:
                out_list.append(word1)
    out_list = list(set(out_list))
    out_list.sort()
    return out_list

if __name__ == '__main__':
    print in_array(a1, a2)
