def Score(a, b, indel, mismatch, match):
    assert len(a) == len(b), "Length of a should be equal to length of b"
    if len(a) == 0 and len(b) == 0:
        return 0
    a_val, b_val = a[0], b[0]
    if a_val == "-" or b_val == "-":
        return indel + Score(a[1:], b[1:], indel, mismatch, match)
    elif a_val == b_val:
        return match + Score(a[1:], b[1:], indel, mismatch, match)
    else:
        return mismatch + Score(a[1:], b[1:], indel, mismatch, match)

a = "AGTTCACAGGCTA-CG"
b = "AGTT-ACATACTAACG"
match = 1
mismatch = -1
indel = -1

print(Score(a, b , indel, mismatch, match))