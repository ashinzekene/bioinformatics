from amino_acid_masses import amino_acid_masses

def Cyclospectrum(masses):
    result = [0]
    masses = [int(mass) for mass in masses]
    accumulator = masses.copy()
    result.extend(accumulator)
    new_accumulator = accumulator.copy()
    for j in range(len(masses) - 2):
        for i in range(len(accumulator)):
            index = (i+j+1) % len(accumulator)
            new_accumulator[i] += accumulator[index]
        result.extend(new_accumulator)
    result.append(sum(accumulator))
    result.sort()
    return result


if __name__ == "__main__":
    peptide_mass = []
    with open("./datasets/dataset_98_4.txt") as f:
        peptide = f.read().strip()
        peptide_mass= [amino_acid_masses[aa] for aa in peptide]
    
    result = Cyclospectrum(peptide_mass)
    
    with open("./results/cyclospectrum_mass.txt", "w") as f:
        f.write(" ".join([str(v) for v in result]))