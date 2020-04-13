from codon_table import codon_table
from translation import Translate
from transcribe import Transcribe, ReverseTranscribe

def PeptideEncoding(nucleotides, expected_peptide):
    nucleotide_length = len(expected_peptide) * 3
    result = []
    rna = Transcribe(nucleotides)
    compliment_rna = Transcribe(nucleotides, True)
    for i in range(len(rna) - nucleotide_length):
        rna_segment = rna[i: nucleotide_length+i]
        peptide = Translate(rna_segment)
        if peptide == expected_peptide:
            result.append(ReverseTranscribe(rna_segment))

    for i in range(len(compliment_rna) - nucleotide_length-1, -1, -1):
        rna_segment = compliment_rna[i: nucleotide_length+i]
        peptide = Translate(rna_segment)
        if peptide == expected_peptide:
            result.append(ReverseTranscribe(rna_segment, True))

    return result


if __name__ == "__main__":
    nucleotides = ""
    peptide = ""
    with open('./datasets/dataset_96_7.txt') as f:
        nucleotides = f.readline().strip()
        peptide = f.readline().strip()

    result = PeptideEncoding(nucleotides, peptide)
    with open('./results/peptide_encoding.txt', 'w') as f:
        f.write('\n'.join(result))
