if __name__ == "__main__":
    peptide_length = 0
    with open('./datasets/dataset_98_3.txt') as f:
        peptide_length = int(f.read().strip())
    
    with open('./results/cyclopedia_sequence.txt', 'w') as f:
        result = peptide_length * (peptide_length - 1)
        f.write(str(result))