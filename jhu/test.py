L1 = [1, 1, 3, 3, 5,5, 7, 7]
L2 = [1, 4, 7, 10]

L3 = []
for el in L1:
	if el in L2 and el not in L3:
		L3.append(el)

print(L3)
