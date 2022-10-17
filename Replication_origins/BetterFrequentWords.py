from collections import defaultdict
def frequency_table(text, k):
    """
    Create a frequency tables for all kmers in a given text. The kmers are the keys and their frequencies are stored
    as the values..

    :param:
        text: string from which the kmers and their frequencies are to be determined
        k: kmer length
    
    :return:
        freq_dict: dictionary with all kmers and their frequencies
    """
    freq_dict = defaultdict(int)
    text_len = len(text)
    for i in range(0, text_len - k):
        kmer = text[i:i+k]
        freq_dict[kmer] += 1
    return freq_dict

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

def better_frequent_words(text, k):
    """
    Less computiational complex algorithm to detect the most frequent words in a text. 
    :param:
        text: text to be analysed
        k: kmer length
    :return:
        freq_words: set of frequent words
    """
    freq_words = set()
    freq_map = frequency_table(text,k)
    max_val = max_map(freq_map)
    for kmer in freq_map.keys():
        if freq_map[kmer] == max_val:
            freq_words.add(kmer)
    return freq_words

def main():
    test_text = 'aactactcatcatcatctcatgatgatagtagctagcgcatgacgttatactcatgcatcgatcgta'
    k = 4
    better_frequent_words(test_text, k)

if __name__ == '__main__':
    main()