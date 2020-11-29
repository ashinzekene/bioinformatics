from collections import defaultdict
from spectrum_convolution import SpectrumConvolution
from leaderboard_cyclopeptide_sequencing import LeaderboardCycloPeptdeSequencing

def ConvolutionCyclopeptideSequencing(spectrum, m, n):
    spectrum.sort()
    convolutions = SpectrumConvolution(spectrum)
    top_convolutions = getTopConvolutions(convolutions, m)
    leader_spectrum = LeaderboardCycloPeptdeSequencing(spectrum, top_convolutions, n)
    return leader_spectrum

def getTopConvolutions(convolutions, m):
    # We're only interested in the masses of amino acids
    convolutions = list(filter(lambda x: x >= 57 and x <= 200, convolutions))
    convolutions_count = defaultdict(int)
    top_m_convolutions = []
    for spectrum in convolutions:
        convolutions_count[spectrum]+=1
    count_index = defaultdict(list)
    for spectrum, count in convolutions_count.items():
        count_index[count].append(spectrum)
    sorted_counts = sorted(count_index.keys())
    count = 0
    pointer = len(sorted_counts) - 1
    while count < m:
        key = sorted_counts[pointer]
        top_m_convolutions += count_index[key]
        count+= len(count_index[key])
        pointer-=1
    top_m_convolutions.sort()
    return top_m_convolutions

if __name__ == "__main__":
    m = 0
    n = 0
    spectrum = []
    with open('./datasets/dataset_104_7.txt') as f:
        m  = int(f.readline())
        n  = int(f.readline())
        spectrum = [int(mass) for mass in f.readline().strip().split(' ')]

    result = ConvolutionCyclopeptideSequencing(spectrum, m, n)
    with open('./results/convolution_cyclopeptide_sequencing.txt', 'w') as f:
        f.write("-".join([str(mass) for mass in result]))
