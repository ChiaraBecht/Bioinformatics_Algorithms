from HammingDistance import calc_hamming_distance
from FrequentWordsMismatches import find_neighbors
from ReverseComplement import reverse_complement_seq

def frequent_words_mismatches_reverse_comp(Text, k, d):
    """
    Find most frequent patterns/kmers/substrings allowing mismatches with at most d mismatches and considering
    reverse complement sequences.

    :param:
        Text: string in which patterns are searched
        k: length of pattern/kmer/substring
        d: mismatch tolerance/number of allowed mismatches
    
    :return:
        result: list of most common patterns
    """
    kmers = []
    neighborhood = set()
    result = []

    for i in range(len(Text) - k + 1):
        kmers.append(Text[i:i+k])

    for i in range(len(Text) - k + 1):
        kmers.append(reverse_complement_seq(Text[i: i + k]))

    for kmer in kmers:
        neighborhood.update(set(find_neighbors(kmer, d)))

    mmax = 0
    for i in neighborhood:
        frequenti = 0
        for c in kmers:
            if calc_hamming_distance(i, c) <= d:
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
    pats = frequent_words_mismatches_reverse_comp(test_text, k, d)
    print(pats)

if __name__ == '__main__':
    main()