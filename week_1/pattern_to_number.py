nucleotide_map = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
}

nucleotide_map_2 = ['A','C','G','T']

def PatternToNumber(pattern):
    number = 0
    len_1 = len(pattern) - 1

    for i in range(len_1):
        number += (4 ** (len_1 - i)) * nucleotide_map[pattern[i]]

    number += nucleotide_map[pattern[len_1]]
    return number

def PatternToNumber2(pattern):
    if pattern == "":
        return 0
    return 4 * PatternToNumber2(pattern[:len(pattern)-1]) + nucleotide_map[pattern[len(pattern) - 1]]

def NumberToPattern(number, t_mers):
    result = ""
    while number > 0:
        result = nucleotide_map_2[number%4]+ result
        number = number // 4

    while len(result) < t_mers:
        result = "A"+ result

    return result


if __name__ == "__main__":
    print(NumberToPattern(8286, 11))
    print(NumberToPattern(5437, 8))
    print(PatternToNumber2("GGAGCTGCACTGGGG"))