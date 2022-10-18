import HammingDistance

def match_pattern_approximately(pattern, text, d):
    """
    Find all start positions where pattern is a substring of the text with not more than d mismatches.

    :param:
        pattern: substring which shall be found in the text
        text: string in which pattern shall be found
        d: number of allowed mismatches
    
    :return:
        start_positions: list of start positions, where the pattern is found in the text
    """
    text_len = len(text)
    pattern_len = len(pattern)
    start_pos_list = []
    for i in range(0, text_len - pattern_len):
        kmer = text[i:i+pattern_len]
        d_hamming = HammingDistance.calc_hamming_distance(kmer, pattern)
        if d_hamming <= d:
            start_pos_list.append(i)
    return start_pos_list

def main():
    test_text = 'catgcatgtcatatgatcttattcgatcatgat'
    pat = 'catg'
    start_position_list = match_pattern_approximately(pat, test_text, 1)
    print(start_position_list)

if __name__ == '__main__':
    main()