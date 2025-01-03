large_list = [i for i in range(1_000_000)]

listcomp = [x*x for x in large_list]
print(listcomp)