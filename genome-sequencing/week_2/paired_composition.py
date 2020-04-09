def PairedComposition(dna, k, d):
    result = []
    for i in range(len(dna) - (2 *k+d)+ 1):
        s2 = i+k+d
        result.append([dna[i:i+k], dna[s2:s2+k]])
    return sorted(result, key=lambda pair: pair[0])

if __name__ == "__main__":
    result = PairedComposition("TAATGCCATGGGATGTT", 3, 2)
    result_string = ""
    for pair in result:
        result_string += "({}|{}) ".format(pair[0], pair[1])
    print(result_string)
