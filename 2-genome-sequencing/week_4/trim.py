from collections import defaultdict
from peptide_scoring import PeptideScoring

def Trim(leaderboard, spectrum, n):
    leaderboard = list(filter(lambda x: x != '', leaderboard))
    if n >= len(leaderboard):
        return leaderboard
    peptide_scores = defaultdict(list)
    new_board = []
    for peptide in leaderboard:
        peptide_scores[PeptideScoring(spectrum, peptide)].append(peptide)
    sorted_keys = sorted(peptide_scores.keys())
    i = 0
    pointer = len(sorted_keys) - 1
    while i < n:
        key = sorted_keys[pointer]
        new_board += peptide_scores[key]
        i+= len(peptide_scores[key])
        pointer-=1
    return new_board

if __name__ == "__main__":
    spectrum = []
    peptides = []
    n = 0
    with open('./datasets/dataset_4913_3.txt') as f:
        peptides = f.readline().strip().split(" ")
        spectrum = [ int(s) for s in f.readline().strip().split(" ")]
        n = int(f.readline())
    
    result = Trim(peptides, spectrum, n)
    with open('./results/trim.txt', 'w') as f:
        f.write(" ".join(result))