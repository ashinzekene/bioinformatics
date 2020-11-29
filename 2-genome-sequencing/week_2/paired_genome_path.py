def PairedGenomePath(pairs, k, d):
    n = len(pairs)
    result = ['*'] * (k + k + n - 1)
    l = k - 1
    for i, pair in enumerate(pairs):
        prefix, suffix = pair.split('|')
        s2 = i+k+d
        result[i:i+l] = list(prefix)
        result[s2:s2+l] = list(suffix)
    return "".join(result)