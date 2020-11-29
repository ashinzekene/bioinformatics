import sys
import os
from collections import defaultdict

sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../week_3"))

from week_3.cyclospectrum_mass import Cyclospectrum

def CyclopeptideScoring(spectrum, peptide_masses):
    score = 1 # for 0
    peptide_spectrum = Cyclospectrum(peptide_masses)
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
    with open('./datasets/dataset_102_3.txt') as f:
        peptide = f.readline().strip()
        spectrum = [ int(s) for s in f.readline().strip().split(" ")]
    
    result = CyclopeptideScoring(spectrum, peptide)
    with open('./results/cyclopeptide_scoring.txt', 'w') as f:
        f.write(str(result))