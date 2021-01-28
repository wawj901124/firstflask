# 排列
from itertools import product
l = [1, 2, 3]
print(list(product(l, l)))
print(list(product(l, repeat=4)))

# 组合
from itertools import combinations
print(list(combinations([1,2,3,4,5], 3)))