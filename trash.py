x = 0
result = []
while x < int(len(seq)):
    if isinstance(seq[x], int):
         result.append(seq[x])
    #if not isinstance(seq[x], list):
    else:
        result.append(list(seq[x]))
    print(x, seq[x], int(len(seq)), type(seq[x]))
    x = x + 1
print(result, list(result).sort)