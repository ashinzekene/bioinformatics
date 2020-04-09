from random import choice
from collections import defaultdict

def EulerianCycle(string_map):
    result = []
    start = choice(list(string_map.keys()))
    stack = [start]
    while len(stack) > 0:
        current = stack[-1]
        if len(string_map[current]) == 0:
            result.insert(0, stack.pop())
        else:
            stack.append(string_map[current].pop())
    return result

if __name__ == "__main__":
    string_map = defaultdict(list)
    with open('./datasets/dataset_203_2.txt') as f:
        lines = f.readlines()
        for line in lines:
            chars = list(map(lambda x: x.strip(), line.split('->')))
            string_map[chars[0]] = chars[1].split(',')

    result = EulerianCycle(string_map)
    
    with open('./results/eulerian_cycle.txt', 'w') as f:
        f.write("->".join(result))
        
        
# 3-> 2

# 0 -> 1 ->2 -4-5-6-9-7-8-6-2-3-0