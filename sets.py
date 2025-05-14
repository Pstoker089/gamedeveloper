"""set={1,"table",True,4.5,11,False,"string","table"}
print(set)
set.add(38)
print(set)
set.remove("table")
print(set)

fs=frozenset(set)"""

#set operations

a={1,2,3,4,5}
b={4,5,6,7,8}

#union of sets
print(a.union(b))
print(a|b)

#intersection of sets
print(a.intersection(b))
print(a&b)

#difference of sets
print(a.difference(b))
print(b-a)

#symetric difference
print(a.symmetric_difference(b))
print(a^b)

