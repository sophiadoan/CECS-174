sequence_start = ''

def find_upstream(dna_sequence):
    gene_start = dna_sequence.find('ATG') #index of where upstream ENDS
    upstream = dna_sequence[0:gene_start]
    upstream_length = len(upstream)
    return [upstream, upstream_length];


def find_gene(dna_sequence):
    global sequence_start
    sequence_start = dna_sequence.find('ATG')
    gene = dna_sequence[sequence_start:]
    atg_start = sequence_start + 1
    genelength = len(gene)
    return [gene, atg_start, genelength];
    
def second_codon(gene_sequence):
    global sequence_start
    secondcodon = gene_sequence[3:6]
    secondcodonloc = sequence_start + 4
    return [secondcodon, secondcodonloc];

def third_codon(gene_sequence):
    global sequence_start
    thirdcodon = gene_sequence[6:9]
    thirdcodonloc = sequence_start + 7
    return [thirdcodon, thirdcodonloc];

def complementary_nucleotide(nucleotide):
    if nucleotide == 'A':
        nucleotide = nucleotide.replace('A', 'T')
    elif nucleotide == 'T':
        nucleotide = nucleotide.replace('T', 'A')
    elif nucleotide == 'G':
        nucleotide = nucleotide.replace('G', 'C')
    elif nucleotide == 'C':
        nucleotide = nucleotide.replace('C', 'G')
    return nucleotide
    
def complementary_sequence(dna_sequence):
    complementary_sequence = ''
    for i in dna_sequence:
        complementary_sequence += complementary_nucleotide(i)
    return complementary_sequence
    
if __name__ == "__main__":
    sequence_input = input("Please enter a DNA genetic sequence: \n")
    print(f"\nOriginal sequence: {sequence_input}\n")

    geneinfo = find_gene(sequence_input)
    gene = geneinfo[0]

    upstreaminfo = find_upstream(sequence_input)
    secondcodoninfo = second_codon(gene)
    thirdcodoninfo = third_codon(gene)


    print(f"ATG codon at bp {geneinfo[1]}")
    print(f"    followed by {secondcodoninfo[0]} at bp {secondcodoninfo[1]}")
    print(f"    followed by {thirdcodoninfo[0]} at bp {thirdcodoninfo[1]}\n")

    print(f"Upstream sequence: {upstreaminfo[0]}")
    print(f"Upstream length:   {upstreaminfo[1]} bp\n")

    print(f"Gene sequence: {gene}")
    print(f"Gene length:   {geneinfo[2]} bp")

    print(f"[+ Strand]: {gene}")
    print(f"            {'|' * geneinfo[2]}")
    print(f"[- Strand]: {complementary_sequence(gene)}\n")


    


