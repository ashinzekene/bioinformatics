def IsUniversalLinear(str_val, k):
    linears = {}
    formatter = "{0:0>%db}" % k
    for i in range(k*k - 1):
        val = formatter.format(i)
        linears[val] = 0

    for i in range(len(str_val) - k + 1):
        val = str_val[i:i+k]
        if val not in linears:
            return False
        if linears[val] != 0:
            return False
        linears[val]+= 1

    for count in linears.values():
        if count != 1:
            return False

    return True

if __name__ == "__main__":
    print(IsUniversalLinear("1000101110", 3))