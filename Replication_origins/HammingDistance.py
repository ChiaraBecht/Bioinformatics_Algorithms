def calc_hamming_distance(string1, string2):
    """
    Calculate the Hamming distance (number of mismatches) between two strings of equal length.

    :param: 
        string1: string to which another string is compared
        string2: string which is compared to string1
    
    :return:
        hamming_distance: the number of mismatches = Hamming distance
    """
    string1 = string1.upper()
    string2 = string2.upper()
    hamming_distance = 0

    if len(string1) == len(string2):
        for i in range(0, len(string1)):
            if string1[i] != string2[i]:
                hamming_distance += 1
    return hamming_distance

def main():
    hamming_dist = calc_hamming_distance('gtcatg', 'gtgatc')
    print(hamming_dist)

if __name__ == '__main__':
    main()