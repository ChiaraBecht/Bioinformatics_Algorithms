def match_pattern(pattern, text):
    """
    Match a given kmer/pattern/substring to a text and get the starting position for each match.

    :param:
        pattern: short sequence for which the starting position of each match in a text shall be obtained
        text: the text to which the pattern shall be matched
    
    :return:
        match_positions: list with all matching start positions
    """
    text_len = len(text)
    pattern_len = len(pattern)
    start_pos_list = []
    for i in range(0, text_len - pattern_len):
        kmer = text[i:i+pattern_len]
        if kmer == pattern:
            start_pos_list.append(i)
    return start_pos_list

def main():
    test_text = 'ttcattgcatgcagctcatgcatcatcatatgcatactatgcatctttaccggg'
    start_positions = match_pattern('cat', test_text)
    print(start_positions)

if __name__ == '__main__':
    main()