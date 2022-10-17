from collections import defaultdict
def frequency_table(text, k):
    """
    """
    freq_dict = defaultdict(int)
    text_len = len(text)
    for i in range(0, text_len - k):
        kmer = text[i:i+k]
        freq_dict[kmer] += 1
    return freq_dict

test_text = 'aactactcatcatcatctcatgatgatagtagctagcgcatgacgttatactcatgcatcgatcgta'



def max_map(freq_dict):
    """
    """
    max_value = max(freq_dict.values())
    max_key = max(freq_dict, key = freq_dict.get)
    print(max_key, max_value)
    return max_value

def better_frequent_words(text, k):
    """
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