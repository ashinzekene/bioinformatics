
def LinearSubPeptideCount(x):
    result = 0
    for i in range(1, x+1):
        if i <= 2:
            result+= 2
        else:
            result+=i
    return result


if __name__ == "__main__":
    x = 0
    with open('./datasets/dataset_100_3.txt') as f:
        x = int(f.read().strip())

    print(LinearSubPeptideCount(x))