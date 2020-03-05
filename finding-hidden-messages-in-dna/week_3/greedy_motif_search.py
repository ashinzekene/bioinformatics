from motif_profile import Profile, ProfileWithLaplace
from profile_most_probable_kmer import ProfileMostProbableKMer
from score import Score


def GreedyMotifSearch2(dnas, k, t):
    bestMotifs = [dna[:k] for dna in dnas]
    for i in range(len(dnas[0]) - k +1):
        kmer = dnas[0][i:i+k]
        motifs = [kmer]
        for dna in dnas[1:]:
            profile_ = Profile(motifs)
            new_motif = ProfileMostProbableKMer(profile_, k, dna)
            motifs.append(new_motif)
        motif_score = Score(motifs)
        best_motifs_score = Score(bestMotifs)

        if motif_score < best_motifs_score:
            bestMotifs = motifs

    return bestMotifs


def GreedyMotifSearch(dnas, k, t):
    bestMotifs = [dna[:k] for dna in dnas]
    for i in range(len(dnas[0]) - k +1):
        kmer = dnas[0][i:i+k]
        motifs = [kmer]
        for dna in dnas[1:]:
            profile_ = ProfileWithLaplace(motifs)
            new_motif = ProfileMostProbableKMer(profile_, k, dna)
            motifs.append(new_motif)
        motif_score = Score(motifs)
        best_motifs_score = Score(bestMotifs)

        if motif_score < best_motifs_score:
            bestMotifs = motifs

    return bestMotifs

    
if __name__ == "__main__":
    dnas = [
        "GAGAGGCAGCACTATCTATACACGTTACATCTGGAATTCCGTAGCAAATGTTGGGTATTAGTTTAAGACAAGAAACCTGACAGGCCGGTCGACCATTAAGGGCGCATTTTTTCTTATAGTAGCCGTGCTAACGGGCCCGCCTGTTGGGATTCACAC",
        "AGTACTGGGGGGTTCATTTTCTTATTAGCCTACGCTCGGGGTACGTCAACAATGTCACCATGAGGGGTATTATCTTGCTGCTTCCAGGAATGGTTTGGGCATAACACCGGGGTCTTGGCGACACTCAGGGTCGCAGAACAAGCAACGCCGCGCCGA",
        "AACTTGGGCTTGTCCGACGCTGGCCTAATGCTATTTGAGCCGATACCGCCGAATTAATGTGCCAAGTTTTGTTCAGGGGTGTTAGCATGCGCTATTGCTTTTAAGTCCTACCACTTCAGCGGGCGTTGGACCACTACCATAGGTCCTAGGACCGAC",
        "CAACGCACCGGGTCAATACGGACATATGCATTTCATTTTCAGACGTATGGCCGTTCTTTCCGCCGAAGCTCCTCATGGGTTTTAGTAATTCATTCAGTTTCGGATTGGATGCTAAAACGGGATTCAAACACAACAGGTAGACTAAATTAGAAACTC",
        "TGTTCCCAGCATGATTGTAGGTAGCCGATTACTTACGATACTGAACAGTTGTGGGTTTTAGATTTGGTGGAATAGATGGAAGGGCATGATTCATCCCCCGTACGAAACTCTCATACGAGCGTGTCGTGGGCTGTACAGAGTTAGGGCAAGCACTTG",
        "GATCGGAGTGGAAGCGGTGACGTCCCATCCTCGTCTTCTAAGCAAGCCCTGTCGGCTGACGTTTGAGGGCTCGCAATAGTCGAACTACCACAACCCAAAGGGCGACTGTACAAGTATATTTATTGGGTTTTAGTGTATAGCGCCGAGCAGGTTCGC",
        "ATTATGGTATACTATTCGGTTAAAGTCATAACGAACTTATGGGTTTTACACTCTCTTGCTCTTATGTAAGACCTGAATGAACCGTAACGAAGTACGCTCTCGTCTAACCAGGCCACCAATTACTGGTGGGAGGCGTCCCAAGTGGGAGGCTTGATC",
        "TCGCGGGTGTTACGAAGGGTTGTCAGTGGGCGGGATGTGCATAGCGAGCCCGAAGCCAGGAAGGCCAATTCAACGTCTAATGTACAAGACCCGCGGGACCGGTCCCCACTGATATCTTCGCCTGGGAGCCGCCTCCTGGATTGCAGCACAGCCATG",
        "TCACCCTACCAACCCTTACATTATATTATCACTACAACTGAGCGAAATCTAGACTTTTCAGACCTACGGTTCGCGCCCTTGACTTTGAGGGTCTTAACCCAGACCATCCACCCCATAGCGGAAACCGGACTCCGCTTTCTCCCCTAGCCAGCTCGC",
        "ACTCGCGTAGATTGTATTGTTGAGCGATTTGTAGGCCGACTACTATCACCGGTTCGAACCTTATTTGGCATTATCAATATCCCCTCCATTGCTTACGGCACGCAGGTCCGTTTAGGTATTATAACCGTGGCATCGCGGGTTTTATATATGACCCAG",
        "CCTGACCTATATTCCCCTTAATCCACCACGAGTCCCTGGTAGCCCCGCTGTAGGGTATTACAACTATCAAAGTCGCACGCAGGCTATAACAGATGTGGCGCCCAACCAGGAGCGCCGAGTACATTCTAGAACACTACCCAGGGAAGTCTCTGCAAT",
        "CTTGATTCTCTTCTGATGTCCGGAGATTAAGCAACGGAACTCAGATCCCAAAATAGGCATAGTGCGGCGTTGACCGCCACACTCTTCCGGGTTTTATCCCACACCATGCTAACAACGCAATACTAGGTGCAGGAAGATCTTCTCCGCATTCAAACT",
        "TAACTGAGACACTTGAAAACTGTTGCCACATTGTGGCATGGTGACCCATGTAGGGTATTAGTGGGCAAACGATCGGACTAGTGTAGTCAGATGCTCCCCATGGTTGACGACTGACCTAAATATAAACCAACGTAATCTGGCCGGTAACTGAAAAAG",
        "ATAGGAACTACTCTAGTATTGCTTTGGTGGGTTTTAGCTTGACGCGCAACGACAACACGAGCGGATCAGAGGACTTCTATAGTTGTATAACCAGGACGATTTATCGCTTTTAGGAGCATACATGAACGCATTTCAAGCGGGCAGATGCGACGAAAA",
        "AGCGCTCCGTTCACAAGACCCTGCTCAGTTCAGGAGCATGTATTTCGTTAGGGGGTTTTAGGGGCAGGCTTAAAGCGTGGCATTCCACTTTTGCGACCAAAACACCAATACACGGAGTCCCACTGATTCATAACCTTCTGGTTGGTTCAGGAATCT",
        "TCCGCAGGAGAGCGCCTGCTGCTTACAAATGGATTGTCGTCTTGCAAGGCTCAACTGTGGGGGTTAAACCTATATTAGATGGTCTAAGGGGTCTTACACTATAACACGCACCTCGCGTCAGCCCCCGTCAGAGGGTTTCGAATTTCAATGTGTTAG",
        "TCCCGCGTGGCCATGCAAGAATATATCGAACTCAAGGGTTCTTGGAACCAAAGGGATCGGCGACAATGGATTGAGGGAAAGCCCACAGTAGCTCGGACCAATCACGCTGTACCGTGTACCTAAAGGGTTTTAACTACTCAAGCCCCTCATGCAGAC",
        "GCCTGCGCGAAAACCAACTTGTCGATGCCCCGATTCGACTCGAGCTATCGACCCGAAACATCTAGCCTTTTTAAGCTTCCGATTCCCGAAGCCAAGAGTCGGATTTCCGTGACCATGGCTCTAGGGCTATCATACGATTGTCTGTTTAGGGTTTTA",
        "GCCTGTTACGGAGCCGCTTGCGCTTCCCAACCCGATTCAAGTTTGGAGAAAGGCACCTGGACTCGAATGTGTCTAGTCTAGCTAATTATGGTGTCGGGATGCCAAGTTTACTGGGTCTTAGAAAATTCCCTCCTCTGTTTTGTCACGTTAACTGTC",
        "AGATCTATCTTTTTTAACGAACTGTGAGATCCATGGTTACTAACGCGATCCCGGGTGTTAAAACTAGCTTGCTATACTATCGTTATCCGTCAGAGCGTACAGCTGGTTTGCCCGGACAACCATGCAAGGTGCGAATCCCCATAAATTTTGTCCGAT",
        "TTATGTGACGCATGTCCTCCCATAGTGGCGGTTACGTATCGGGTTTTACTCGAATTTGATCGAATAACCGGAACCACTGGCGACAAGACTGACCCCCGACGAGTCAGGTCGTTCTAGTAGGGTAGTACCATATGCCCATGTTACGTAAGATCTATT",
        "GGTTCGACCTGGGCACCTTGCTACTGGTGGGTCTTAGAACGTTTGATGTGGTGGAAAATGGTGGAGTGTCACATGCCGTTGTCAACACCCGCACATTGGCCAGATGCCGTGTGCTTACACACTATATCTTTCTCGTTAAATTTTTGTTGTCACTAC",
        "GCCTTGCGACCTATTTCGCCCGTGTCCAGGGTTTTAGTTGCGGAGCCGGAGCTCCGCAATGGCCTCCTCGTCGGATACAGCGCCAGCCGTACCGCACAATAAGACAGGATATAGAAACGAGGTTCTCTTAGGACTCGCAGTAGGAGCGTGCAGGGG",
        "GGCATGTGGAATCTCTTGAGGAAAATCACAGGAAAGACTTTTATACCAGTCACCTGGGCGCCCGGCGACCGGCGTCACAATCTCTAGGAGCCTGCGTGGTGAGTCATTTACTGGGTCTTACCCGAATAAGCGGAGTGTACAGGGGGATCTTGAGTT",
        "CAAGGAAGGAGGGTCACGCGGGCGGAGGCATGGCAGTTGGCCTGTCTCCTAAGCCATTCGCGTGCCTGGCTCTTGAGGGTCTTAAAAAAGCTTGGGTCGCGGGTAAGGTACGATGATAGCAAGACTCTCTATGTATCAGTATCCCGGTAAGGACAG",
    ]
    result = GreedyMotifSearch(dnas, 12, 25)
    print(" ".join(list(map(str, result))))