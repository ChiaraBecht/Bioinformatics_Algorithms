def reverse_complement_seq(DNA_seq):
    """
    """
    base_pairings = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    sequence = DNA_seq.lower()
    sequence_comp_list = []
    for base in sequence:
        comp_base = base_pairings[base]
        sequence_comp_list.append(comp_base)
    sequence_comp = ''.join(sequence_comp_list)
    sequence_comp_rev = sequence_comp[::-1]
    rev_comp_DNA_seq = sequence_comp_rev.upper()

    return rev_comp_DNA_seq

def main():
    test = 'ACATGCATGCGTACGTACCGG'
    Seq_comp_rev = reverse_complement_seq(test)
    print(Seq_comp_rev)

if __name__ == '__main__':
    main()