from collections import defaultdict

def EulerianPath(string_map):
    result = []
    start = GetStart(string_map)
    stack = [start]
    while len(stack) > 0:
        current = stack[-1]
        if len(string_map[current]) == 0:
            result.insert(0, stack.pop())
        else:
            stack.append(string_map[current].pop())
    return result


def GetStart(string_map):
    result  = dict()
    for k, v in string_map.items():
        if k not in result != 2:
            result[k] = [0, 0]
        result[k][0] = len(v)
        for val in v:
            if val not in result != 2:
                result[val] = [0, 0]
            result[val][1]+=1
    for i, edges in result.items():
        if edges[0] > edges[1]:
            return i

    return list(result.keys())[0]


if __name__ == "__main__":
    string_map = defaultdict(list)
    with open('./datasets/dataset_203_6.txt') as f:
        lines = f.readlines()
        for line in lines:
            chars = list(map(lambda x: x.strip(), line.split('->')))
            string_map[chars[0]] = chars[1].split(',')

    result = EulerianPath(string_map)
    with open('./results/eulerian_path.txt', 'w') as f:
        f.write("->".join(result))
        
        
# 3-> 2

# 0 -> 1 ->2 -4-5-6-9-7-8-6-2-3-0