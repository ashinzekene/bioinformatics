import sys
import os
from collections import defaultdict

sys.path.append(os.path.abspath(".."))

from week_3.amino_acid_masses import amino_acid_masses
from cyclopeptide_scoring import CyclopeptideScoring
from linearpeptide_scoring import LinearPeptideScoring

def LeaderboardCycloPeptdeSequencing(spectrum, masses, n):
    leaderboard = [[]]
    leader_peptide = ''
    leader_peptide_score = 0
    parent_mass = max(spectrum)
    while len(leaderboard):
        leaderboard = expand(leaderboard, masses)
        for i, peptide in enumerate(leaderboard):
            peptide_mass = Mass(peptide)
            if peptide_mass == parent_mass:
                peptide_score = CyclopeptideScoring(spectrum, peptide)
                if peptide_score > leader_peptide_score:
                    leader_peptide = peptide
                    leader_peptide_score = peptide_score
            elif peptide_mass > parent_mass:
                leaderboard[i] = ''
        leaderboard = trim(leaderboard, spectrum, n)
    print('Leader peptide score', leader_peptide_score)
    return leader_peptide

def Mass(peptide_mass):
    return sum(peptide_mass)

def expand(leaderboard, masses):
    new_leaderboard = []
    for peptide in leaderboard:
        for mass in masses:
            new_peptide = peptide + [mass]
            new_leaderboard.append(new_peptide)
    return new_leaderboard


def trim(leaderboard, spectrum, n):
    leaderboard = list(filter(lambda x: x != '', leaderboard))
    if n >= len(leaderboard):
        return leaderboard
    peptide_scores = defaultdict(list)
    new_board = []
    for peptide_mass in leaderboard:
        peptide_scores[LinearPeptideScoring(spectrum, peptide_mass)].append(peptide_mass)
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
    n = 0
    spectrum = []
    masses = list(set(amino_acid_masses.values()))
    with open('./datasets/tyrocidine_b1_10.txt') as f:
        n = int(f.readline().strip())
        spectrum = [ int(s) for s in f.readline().strip().split(" ")]

    result = LeaderboardCycloPeptdeSequencing(spectrum, masses, n)
    list_result = '-'.join([str(k) for k in result])
    with open('./results/leaderboard_cyclopeptide_sequencing_tyrocidine_b1_10.txt', 'w') as f:
        f.write(list_result)
