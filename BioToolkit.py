# Function that validate sequence
def validate_seq(seq):
    """ This function validates sequence"""
    allowed_nucs = ['A','G','T','C','U']
    illegal_nucs = {}
    seq = seq.upper()
    for ind, nuc in enumerate(seq):
        if nuc not in allowed_nucs:
            illegal_nucs[ind] = nuc
    if illegal_nucs:
        print('Illegal nucleotide found')
        return illegal_nucs
    else:
        print("Valid Nucleotide Sequece")
        return seq

# let' write another function that counts all the nucleotide bases
def Nuc_Count(seq):
    count_dict = {"A":0,"G":0,"T":0,"U":0,"C":0}
    for nuc in seq:
        count_dict[nuc]+=1
    return count_dict

# let's write a transcription function
def transcribe(seq):
    seq.replace("T","U")
    return seq

# let's write a reverse_complement function
def reverse_comp(seq):
    """Reverse complement a dna strand"""
    # map_dict = {
    #     "A": "T",
    #     "T": "A",
    #     "G": "C",
    #     "C": "G",
    # }
    # return "".join([map_dict[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG','TAGC')
    return seq.translate(mapping)[::-1]

# function that generates random DNA sequence
def DNA_generator(length):
    """Generates random DNA based on the length you provide"""
    import random
    nucs_set = ["A","T","G","C"]
    Sequence = "".join([random.choice(nucs_set) for i in range (length)])
    return Sequence

# function that finds gc_percentage
def gc_percent(seq):
    seq = seq.upper()
    gc_cent = (seq.count("G")+seq.count('C') )/(len(seq))*100
    return int(gc_cent)

# motif finding funtion
def find_motif(seq,motif):
    posititions = []
    for i in range(len(seq)-len(motif)+1):
        if seq[i:i+len(motif)] == motif:
            posititions.append(i)
    if not posititions:
        print('No Match for the motif')
    else:
        return posititions

# k-mer calculation
def k_mers(seq,kmer_len=3):
    kmer_counter = {}
    for i in range(len(seq)-kmer_len+1):
        kmer = seq[i:i+kmer_len]
        kmer_counter[kmer] = kmer_counter.get(kmer,0)+1
    if not kmer_counter:
        print("No such kmer found")
    else:
        print(f"We found {len(kmer_counter)} {kmer_len} bases subsequence in your main sequence")
        return kmer_counter

# translation function:
def translate_seq(seq):
    protein = ""
    codon_dict = {
        "ATG": "M", 
        "TTT": "F",
        "AAA": "G",
        "TAA": "*",
        "TAG":"*",
        "TGA":"*"}
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        protein+=(codon_dict.get(codon,"?"))
    return protein

# open reading frame function
def ORF(seq):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    position_tracker = []
    # loops to look for start codon in the sliding door technique:
    for i in range(len(seq)-2):
        if seq[i:1+3] == start_codon:
            protein = ""
            for J in range(i,len(seq),3):
                codon = seq[J:J+3]
                if len(codon)<3: # short possibly at the end of the current sequecne 
                    break
                if codon in stop_codons:
                    protein += codon
                    position_tracker.append(
                        {"start":i,
                         'end':i+J,
                         "protein":protein}
                    )
                    break
                protein+= codon
