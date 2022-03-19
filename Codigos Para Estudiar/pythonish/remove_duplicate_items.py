"""
l = [1,2,2,3,4,4,3]
res = []
for i in l:
    if i not in res:
        res.append(i)
print(res)
"""

l = [1, 2, 2, 3, 4, 4, 3]
res = list(set(l))
print(res)
