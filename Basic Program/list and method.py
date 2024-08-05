# List can be changed and modified using various operations


l1 = [ 465,5,34,566,"omendra"]

print(type(l1))
print(l1)
l1.remove("omendra")
print(l1)
print(l1.count(34))
l1.sort()
print(l1)
l1.pop()
print(l1)
l1.append(78)
print(l1)


l2 = [89,73,43,23]
l1.extend(l2)
print(l1)

l1.sort()
print(l1)

print(l1[0:4])