#Create a large list
large_list = [i for i in range(1_000_000)]

#Use list comp to multiply the number by itself
list_comp = [x*x for x in large_list]
print(list_comp)