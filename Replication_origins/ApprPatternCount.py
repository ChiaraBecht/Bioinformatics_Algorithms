import HammingDistance

def approximate_pattern_count(Text, pattern, d):
    """
    
    """
    count = 0
    for i in range(0, len(Text) - len(pattern)):
        pat = Text[i:i + len(pattern)]
        if HammingDistance.calc_hamming_distance(pattern, pat) <= d:
            count += 1
    return count

def main():
    test_text = 'catgcatgtcatatgatcttattcgatcatgat'
    pat = 'catg'
    apr_pat_count = approximate_pattern_count(test_text, pat, 1)
    print(apr_pat_count)

if __name__ == '__main__':
    main()