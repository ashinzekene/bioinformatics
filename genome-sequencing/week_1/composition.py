def Composition(dna, k):
    result = []
    for i in range(len(dna) - k+1):
        result.append(dna[i:i+k])
    return result

if __name__ == "__main__":
    text = ""
    k = 0
    with open('./datasets/dataset_197_3.txt') as f:
        k = int(f.readline())
        text = f.readline().strip()

    with open('./results/composition.txt', 'w') as f:
        f.write(
            "\n".join(Composition(text, k))
        )
