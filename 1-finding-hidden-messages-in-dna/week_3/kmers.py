nucleotides = ["A", "C", "G", "T"]
def Kmers(k):
    result = []
    generateKmers(k, 0, "", result)
    return result

def generateKmers(k, l, string, result):
    if k == l:
        result.append(string)
    else:
        for nucleotide in nucleotides:
            generateKmers(k, l+1, string + nucleotide, result)
            
if __name__ == "__main__":
    print(Kmers(3))