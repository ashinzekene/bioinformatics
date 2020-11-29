
nucleotides = {"A":0, "C":1, "G":2, "T":3}
def ProfileMatrix(profile, motif) :
    result = 1
    for i in range(len(motif)):
        p = nucleotides[motif[i]]
        result *= profile[p][i]
    
    return result
    
    


if __name__ == "__main__":
    A = [
        [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
        [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
        [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
        [0.3, 0.1, 0.0, 0.4, 0.5, 0.0],
    ]
    print(ProfileMatrix(A, "CAGTGA"))