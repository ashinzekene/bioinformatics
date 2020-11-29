from amino_acid_masses import amino_acid_masses

def LinearSpectrum(peptide):
    prefix_mass = [0] * (len(peptide) + 1)
    for i, aa in enumerate(peptide):
        prefix_mass[i+1] = prefix_mass[i] + amino_acid_masses[aa]
    
    linear_spectrum = [0]
    for i in range(len(prefix_mass)):
        for j in range(i+1, len(prefix_mass)):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    linear_spectrum.sort()
    return linear_spectrum




if __name__ == "__main__":
    peptide = ""
    with open("./datasets/dataset_4912_2.txt") as f:
        peptide = f.read().strip()
    
    result = LinearSpectrum(peptide)
    
    with open("./results/linear_spectrum.txt", "w") as f:
        f.write(" ".join([str(v) for v in result]))