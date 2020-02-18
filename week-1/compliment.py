def Compliment(text):
    result = ""
    nucleotide_map = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }
    for i in text:
        result = nucleotide_map[i] + result
    return result
    
if __name__ == "__main__":
    text = input("Enter text: \n").strip()
    print(Compliment(text))