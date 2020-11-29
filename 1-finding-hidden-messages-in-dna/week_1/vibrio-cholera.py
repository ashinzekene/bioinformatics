from pattern_match import PatternMatch

pattern = "CTTGATCAT"

result = ""
with open('./resources/Vibrio_cholerae.txt') as f:
    lines = f.readlines()
    for line in lines:
        result += PatternMatch(line, pattern) + " "
        
with open('./results/vibro.txt', 'w') as f:
    f.write(result)

print("Done!")