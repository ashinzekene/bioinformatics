def FrequentWords(Text, k):
    str_dict = {}
    for i in range(len(Text) - k+1):
        if str_dict.get(Text[i:i+k]) == None:
            str_dict[Text[i:i+k]] = 1
        else:
            str_dict[Text[i:i+k]] += 1
    
    max_count = 0
    for pattern, count in str_dict.items():
        max_count = max(max_count, count)
    
    result = []
    for pattern, count in str_dict.items():
        if count == max_count:
            result.append(pattern)
    
    return result

if __name__ == "__main__":
    string = input("Enter string: \n").strip()
    count = int(input("Enter count: \n").strip())

    print(FrequentWords(string, count))
