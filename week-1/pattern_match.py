def PatternMatch(Pattern, Genome):
    result = []
    for i in range(len(Genome) - len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            result.append(i)

    return result

if __name__ == "__main__":
    Genome = input("Enter genome: \n").strip()
    Pattern = input("Enter pattern: \n").strip()
    print(PatternMatch(Pattern, Genome))
