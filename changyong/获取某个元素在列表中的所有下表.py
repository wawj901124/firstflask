lst = [114, 514, 19, 19, 114, 123, 114, 12342354235]
toFind = 114
print(list(filter(lambda x: lst[x]==toFind, list(range(len(lst))))))   #利用list(range(len(lst)))创建下标列表，再利用filter函数筛选出所有满足条件的下标。