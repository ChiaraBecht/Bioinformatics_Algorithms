def find_min_skew(text):
    """
    find all integers i which minimize the skew over i of the genome. The skew is here defined as the difference
    of Guanine and Cytosine: Skewi(genome) = Gi - Ci. The minimum skew values i mark locations, where the origin
    of the genome under test could be located.

    :param:
        text: DNA string derived from the genome for which the origin shall be find
    
    :reuturn:
        i_values: all integers i, which minimize skewi(genome)
    """
    skew = 0
    i_values = []
    for id in range(0, len(text)):
        if text[id] == 'G':
            skew += 1
        if text[id] == 'C':
            skew -= 1
        i_values.append(skew)
    print(i_values)

    min_i_values = min(i_values)
    i_return = [i for i, j in enumerate(i_values) if j == min_i_values]
    print(min_i_values)
    return i_return

def main():
    i_return = find_min_skew('CATGGGCATCGGCC')
    print(i_return)

if __name__ == '__main__':
    main()