from codon_table import codon_table
        
def Translate(nucleotides):
    polypeptide = ""
    for i in range(0, len(nucleotides)-2, 3):
        codon = nucleotides[i: i+3]
        polypeptide += codon_table[codon]
    return polypeptide


if __name__ == "__main__":
    nucleotides = ""
    with open('./datasets/dataset_96_4.txt') as f:
        nucleotides = f.read().strip()

    polypeptide = Translate(nucleotides)

    with open('./results/translation.txt', 'w') as f:
        f.write(polypeptide)