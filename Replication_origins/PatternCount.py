def count_pattern(text, pattern):
    """
    count the frequency of a given pattern in a given text
    :param:
        text: given text as a string, which shall be analyzed
        pattern: the search pattern whoms occurences are counted in the text
    
    :return:
        count: number of occurences of the pattern
    """
    count = 0
    kmer_len = len(pattern)
    text_len = len(text)
    upper_limit = text_len - kmer_len
    for i in range(0, upper_limit):
        kmer = text[i:i+kmer_len]
        if kmer == pattern:
            count += 1
    return count

def main():
    test_text = 'aactactcatcatcatctcatgatgatagtagctagcgcatgacgttatactcatgcatcgatcgta'
    test_pattern = 'cat'
    counts = count_pattern(test_text, test_pattern)
    print(counts)

if __name__ == '__main__':
    main()