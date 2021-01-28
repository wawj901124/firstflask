import itertools
aa = ['titte', 'url', 'acture', 'result']
bb = list(itertools.permutations(aa, 2))  #排列有序组合
print(bb)
print("######################")
cc = list(itertools.combinations(aa, 2))  #无序组合
print(cc)