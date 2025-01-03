s = {"Python","Java","PhP","Android","Java"}
n = {2,3,4,5,6,7,8,9,0,True,1,False}
# print(s)
# print(n)

# for i in s:
#     print(i)

# s.add("Node")
# s.update(n)

# s.remove("React")
# s.discard("React")
# ritme =  s.pop()
# print(ritme)
# print(s)

set1 = {"a", "b", "c",True}
set2 = {1, 2, 3,"a"}

# set3 = set1.union(set2)
# set3 = set1 | set2
# set3 = set1.intersection(set2)
# set1.intersection_update(set2)
# set3 =  set1.intersection(set2)
# set3 = set2.difference(set1)
set3 = set1.symmetric_difference(set2)

print(set3)