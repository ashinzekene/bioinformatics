from clump_finder import ClumpFinder

pattern = "CTTGATCAT"

result = ""
L = 500
k = 9
t = 3

result = []
with open('./resources/E_coli.txt') as f:
    lines = f.readlines()
    for line in lines:
        mers = ClumpFinder(line, L, k, t)
        result += mers

with open('./results/E_coli.txt', 'w') as f:
    f.write(" ".join(map(str, result)))

print("Done!", len(mers))