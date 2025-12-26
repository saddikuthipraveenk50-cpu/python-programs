from itertools import combinations

def all_subsets(lst):
    res = []
    for r in range(len(lst)+1):
        for combo in combinations(lst, r):
            res.append(list(combo))
    return res

print(all_subsets([1,2,3]))
