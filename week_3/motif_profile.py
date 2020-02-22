nucleotide_index = {'A':0,'C':1,'G':2, 'T':3 }

def Profile(motifs):
    profile = [[0] * len(motifs[0]) for i in range(4)]
    for i in range(len(motifs[0])):
        for motif in motifs:
            index = nucleotide_index[motif[i]]
            profile[index][i]+=1/len(motifs)
    
    return profile

def ProfileWithLaplace(motifs):
    profile = [[1] * len(motifs[0]) for i in range(4)]
    for i in range(len(motifs[0])):
        for motif in motifs:
            index = nucleotide_index[motif[i]]
            profile[index][i]+=1/len(motifs)
    
    return profile

if __name__ == "__main__":
    print(Profile([
        "GGC",
        "AAG"
    ]))