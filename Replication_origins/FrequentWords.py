import PatternCount as PC
def find_frequent_patterns(text, k):
    """
    Given a text and a kmer length, find the most frequent patterns (substrings of kmer length) in the text.
    
    :param:
        text: text which shall be analyzed for its most frequent patterns
        k: length of the substrings/kmers
    
    return:
        frequent_pattern: a set of frequent patterns
    """
    frequent_patterns = set()
    text_len = len(text)
    count = []
    
    for i in range(0, text_len - k):
        pattern = text[i:i+k]
        count.append(PC.count_pattern(text, pattern))
    max_count = max(count)
    #max_index = count.index(max_count)
    for i in range(0, text_len - k):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    return frequent_patterns

def main():
    test_text = 'aactactcatcatcatctcatgatgatagtagctagcgcatgacgttatactcatgcatcgatcgta'
    k = 4
    freq_pat = find_frequent_patterns(test_text, k)
    print(freq_pat, type(freq_pat))

if __name__ == '__main__':
    main()