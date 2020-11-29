nucleotide_map = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"
}

reverse_nucleotide_map = {
    "U": "A",
    "A": "T",
    "C": "G",
    "G": "C",
}

def Transcribe(nucleotides, reverse=False):
    compliment = ""
    if not reverse:
        return nucleotides.replace("T", "U")
    for base in nucleotides[::-1]:
        compliment += nucleotide_map[base]
    return compliment


def ReverseTranscribe(nucleotides, reverse=False):
    compliment = ""
    if not reverse:
        return nucleotides.replace("U", "T")
    for base in nucleotides[::-1]:
        compliment += reverse_nucleotide_map[base]
    return compliment

