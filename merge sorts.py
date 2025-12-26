def merge_sorted(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    return res + a[i:] + b[j:]

print(merge_sorted([1,4,6],[2,3,5]))
