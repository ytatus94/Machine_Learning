#!/usr/bin/python

# Part 1
def valid_strands(dna_strands):
    # Check single strand
    def strand_length(strand):
        if len(strand) > 10 and len(strand) < 100:
            return True
        else:
            return False

    def strand_contains_ATGC(strand):
        for i in strand:
            if i not in ['A', 'T', 'G', 'C']:
                return False
        return True

    def strand_uppercase(strand):
        if strand.isupper():
            return True
        else:
            return False

    # Select a valid strand
    clean_strands = []
    for strand in dna_strands:
        length = strand_length(strand)
        ATGC = strand_contains_ATGC(strand)
        uppercase = strand_uppercase(strand)
        if length and ATGC and uppercase:
            clean_strands.append(strand)

    if len(clean_strands) < 3:
        return ''
    else:
        return clean_strands


# Part 2
def overlap_strands(clean_strands):
    new = []
    while len(clean_strands) > 0:
        strand = clean_strands.pop()
        if len(new) == 0:
            new.append(strand)
        else:
            if strand[:3] == new[-1][-3:]:
                # the first three characters in the strand == the last three characters in the last element
                # appand the strand at the end of the new list
                new.append(strand)
            elif strand[-3:] == new[0][:3]:
                # the last three characters in the strand == the first three characters in the first element
                # insert the strand to the beginning of the new list
                new.insert(0, strand)
            else:
                # if not the cases, put strand back to the clean_strands
                # because we use pop() to pop the last element in clean_strands
                # we have to insert the strand to the beginning of clean_strands
                # if we use push() then it becomes an infinit loop
                clean_strands.insert(0, strand)
    # print(new)
    # combine strings and remove repeated characters
    if len(new) == 0:
        return ''
    new_str = new[0]
    for i in range(1, len(new)):
        new_str += new[i][3:]
    return new_str


# part 3
def mapping(string, codon_mapping):
    # Split the string by every three characters
    splited_str = [string[i:i+3] for i in range(0, len(string), 3)]

    # Count the results
    count = {}
    for i in splited_str:
        if i in codon_mapping.keys():
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1

    # Change key name
    new_dict = {}
    for k in count.keys():
        new_dict[codon_mapping[k]] = count[k]

    # print sorted dictionary
    output_str = ''
    for k, v in sorted(new_dict.items(), key=lambda x: x[0]):
        # print('{}: {}'.format(k, v))
        output_str += '{}: {}\n'.format(k, v)

    # remove the last new line character
    output_str = output_str[:-1]
    print(output_str)


def main():
    dna = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT']
    # dna = ['AGTGGGGGGGGG', 'AAACCCAATTT']
    # dna = ['', '    ', 'ACGTATGATTTTT', 'AGTVA','Atgc', '123', 'ATTTTAGGGGGAA']
    # dna = ['', '    ', 'ACGTATGATTTTT', 'AGTVA','Atgc', '123', 'TTTAGGGGGAAT', 'ATTTAAACACG']
    # dna = ['AATTGGCCAATTG', 'TTGAATTGGCCAAAA', 'AAATTTGGGCCC', 'AAAEEERRRTTT', 'NEWUSER123']
    # dna = ['XYZ']
    # dna = ['AGTCCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT', 'AGTGGGGGGGGG', 'GGGAATATCTATCATTACATTTTAC',
    #        'TACTATCACTACTTACT', 'ACTATCTATTACTGGGTGAT', 'GATTACTATGTGACGTACGGTACG', 'ACGGGGCAGCAGGGTGCCGT']

    clean = valid_strands(dna)
    print(clean)

    overlap = overlap_strands(clean)
    print(overlap)

    codon_mapping = {'AAA': 'Lysine', 'GGG': 'Glycine', 'TTT': 'Phenylalanine'}
    # mapping(overlap, codon_mapping)
    mapping('AAATTTGGGAAA', codon_mapping)

if __name__ == '__main__':
    main()
