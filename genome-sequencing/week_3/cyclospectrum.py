from amino_acid_masses import amino_acid_masses

def Cyclospectrum(peptide):
    result = [0]
    masses = [amino_acid_masses[amino_acid] for amino_acid in peptide]
    accumulator = masses.copy()
    result.extend(accumulator)
    new_accumulator = accumulator.copy()
    for j in range(len(peptide) - 2):
        for i in range(len(accumulator)):
            index = (i+j+1) % len(accumulator)
            new_accumulator[i] += accumulator[index]
        result.extend(new_accumulator)
    result.append(sum(accumulator))
    result.sort()
    return result


if __name__ == "__main__":
    peptide = ""
    with open("./datasets/dataset_98_4.txt") as f:
        peptide = f.read().strip()
    
    result = Cyclospectrum(peptide)
    
    with open("./results/cyclospectrum.txt", "w") as f:
        f.write(" ".join([str(v) for v in result]))