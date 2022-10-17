def reverse_complement_seq(DNA_seq):
    """
    For a given DNA sequence find its reverse complement. This sequence is the complement sequence written out
    in the same direction as the template strand.
    
    :param:
        DNA_seq: the target sequence for which the reverse complement shall be computed
    
    :return:
        rev_comp_DNA_seq: reverse complement of the entered sequence
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