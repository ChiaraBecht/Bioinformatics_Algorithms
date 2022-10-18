import HammingDistance

def find_neighbors(pattern, d):
    """
    Find the neighborhood set for a kmer

    :param:
        pattern: kmer for which we want to find the neighboring kmers with d or less mismatches
        d: number of allowed mismatches
    """
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    neighbor= []
    suffixneighbors = find_neighbors(pattern[1:], d)
    for text in suffixneighbors:
        if HammingDistance.calc_hamming_distance(pattern[1:], text) < d:
            for x in ["A", "C", "G", "T"]:
                neighbor.append(x + text)
        else:
            neighbor.append(pattern[0] + text)

    return neighbor

def max_map(freq_dict):
    """
    Find the maximum frequency in the dictionary

    :param:
        freq_dict: dictionary with all kmers and their frequencies derived from  a text of interest
    
    :return:
        max_value: maximum frequency detected
    """
    max_value = max(freq_dict.values())
    max_key = max(freq_dict, key = freq_dict.get)
    print(max_key, max_value)
    return max_value

def frequent_words_mismatches(Text, k, d):
    """
    :param:
        Text: string in which words shall be found
        k: length of kmer
        d: number of allowed mismatches
    :return:
    """
    kmers = []
    neighborhood = set()
    result = []

    for i in range(len(Text) - k + 1):
        kmers.append(Text[i: i + k])
    for kmer in kmers:
        neighborhood.update(set(find_neighbors(kmer, d)))
    mmax = 0
    for i in neighborhood:
        frequenti = 0
        for c in kmers:
            if HammingDistance.calc_hamming_distance(i, c) <= d:
                frequenti += 1

        if mmax < frequenti:
            mmax = frequenti
            result = [i]
        elif mmax == frequenti:
            result.append(i)
    return result
    
def main():
    test_text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    d = 1
    pats = frequent_words_mismatches(test_text, k, d)
    print(pats)

if __name__ == '__main__':
    main()