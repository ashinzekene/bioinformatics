import sys
import os

sys.path.append(os.path.abspath("."))

from week_4.gibbs_sampler2 import gibbs_sampler

dnas = []
k = 20

with open('./week_5/mtb.txt') as file:
    for line in file:
        if not line.startswith('>'):
            dnas.append(line.strip())

print('Working...')
motif, score = gibbs_sampler(dnas, k, len(dnas), 500)
print(motif, score)