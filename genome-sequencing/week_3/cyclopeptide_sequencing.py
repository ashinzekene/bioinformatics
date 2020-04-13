from amino_acid_masses import amino_acid_masses
from linear_spectrum import LinearSpectrum
from cyclospectrum import Cyclospectrum

masses = list(set(amino_acid_masses.values()))
aa = list(amino_acid_masses.keys())

def CycloPeptideSequencing(spectrum):
    final_peptides = []
    candidate_subpeptides = ['']
    parent_mass = ParentMass(spectrum)
    while len(candidate_subpeptides):
        candidate_subpeptides = expand(candidate_subpeptides)
        for i, peptide in enumerate(candidate_subpeptides):
            if peptide in final_peptides:
                continue
            if Mass(peptide) == parent_mass:
                if Cyclospectrum(peptide) == spectrum:
                    final_peptides.append(peptide)
                else:
                    candidate_subpeptides[i] = ''
            elif not isConsistent(peptide, spectrum):
                candidate_subpeptides[i] = ''
        candidate_subpeptides = list(filter(lambda x: x != '', candidate_subpeptides))
    return final_peptides


def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for amino_acid in aa:
            new_peptides.append(peptide + amino_acid)
    return new_peptides

def Mass(peptide):
    mass = 0
    for aa in peptide:
        mass += amino_acid_masses[aa]
    return mass

def ParentMass(spectrum):
    return max(spectrum)

def isConsistent(peptide, spectrum):
    linear_spectrum = LinearSpectrum(peptide)
    for mass in linear_spectrum:
        if mass not in spectrum:
            return False
    return True


if __name__ == "__main__":
    spectrum = []
    with open('./datasets/dataset_100_6.txt') as f:
        spectrum = f.read().strip().split(' ')
        spectrum = [int(mass) for mass in spectrum]

    result_as_masses = {}
    results = CycloPeptideSequencing(spectrum)
    for result in results:
        mass = "-".join([str(amino_acid_masses[aa]) for aa in result])
        result_as_masses[mass] = True

    with open('./results/cyclopeptide_sequencing.txt', 'w') as f:
        f.write(" ".join(list(result_as_masses.keys())))
