import sys
import os

sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../week_3"))

from week_3.amino_acid_masses import amino_acid_masses
from week_3.linear_spectrum_mass import LinearSpectrum

def PeptideScoring(spectrum, peptide):
    score = 1 # for 0
    peptide_mass = [amino_acid_masses[aa] for aa in peptide]
    peptide_spectrum = LinearSpectrum(peptide_mass)
    pointer = 0
    for mass in peptide_spectrum:
        i = pointer+1
        while i < len(spectrum):
            if spectrum[i] > mass:
                break
            if spectrum[i] == mass:
                score+=1
                pointer = i
                break
            i+=1
            
    return score


if __name__ == "__main__":
    spectrum = []
    peptide = ""
    with open('./datasets/dataset_4913_1.txt') as f:
        peptide = f.readline().strip()
        spectrum = [ int(s) for s in f.readline().strip().split(" ")]
    
    result = PeptideScoring(spectrum, peptide)
    with open('./results/peptide_scoring.txt', 'w') as f:
        f.write(str(result))