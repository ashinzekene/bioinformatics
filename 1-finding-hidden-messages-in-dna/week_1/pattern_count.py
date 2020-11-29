def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern)):
        if Text[i:i+len(Pattern)] == Pattern:
            count+=1
    return count

if __name__ == "__main__":
    text = input("Enter text: \n").strip()
    pattern = input("Enter pattern: \n").strip()
    print(PatternCount(text, pattern))