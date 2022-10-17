from BetterFrequentWords import frequency_table
def find_clumps(text, k, L, t):
    """
    Find every k-mer that forms a clump in the genome. Here window of fixed length
    L is slid along the genome. For each window the k-mer clumps are detected.
    The frequency, defining a clump is defined by parameter t.

    :param:
        text: genome/text for which kmers that form clumps shall be found
        k: length of pattern/kmer
        L: window size
        t: frequency of a kmer to be counted as a clump
    
    :return:
        set of clumps
    """
    patterns = set()
    n = len(text)
    for i in range(0, n - L):
        window = text[i:i + L]
        freqMap = frequency_table(window, k)
        for key in freqMap.keys():
            if freqMap[key] >= t:
                patterns.add(key)
    return patterns

def main():
    test_text = 'gatcagcataagggtccCTGCAATGCATGACAAGCCTGCAGTtgttttac'
    k = 4
    L = 25
    t = 3
    patterns = find_clumps(test_text,k, L, t)
    print(patterns)

if __name__ == '__main__':
    main()