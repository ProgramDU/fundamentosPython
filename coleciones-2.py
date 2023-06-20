# tuplas
#(item1, item2, itemN)
#inmuntables
my_tuple = ("uno", 2, 3.1, False)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
#error 
#my_tuple[0] = "nuevo valor"

#conjuntos set
#(item1, item2, itemN)
#coleccion sin indice y sin duplicados

my_set = {1, 2, 2, 2, 3, 4, "uno"}
print(type(my_set))
print(my_set)
my_set.add(5)

a= {1,2,3,4}
b={4, 5, 6, 7}
print(a. union (b))
print(a.intersection(b))
print(a.difference(b))