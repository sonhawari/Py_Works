

# import time

# def c_to_f(c):
	# return c*9/5 + 32
	
# t0 = time.clock()
# c_to_f(100000)
# t1 = time.clock() - t0
# print("t = ", t, ":", t1, "s,")



# linear search on unsorted list

# def linear_search(L, e):
	# found = False
	# for i in range(len(L))
		# if e == L[i]
			# found = True
	# return found

	
# # linear search on sorted list

# def search(L, e):
	# for i in range(len(L))
		# if L[i] == e:
			# return True
		# if L[i] > e:
			# return False
	# return False

	
	
# linear complexity
def addDigits(s):
	val = 0
	for c in s:
		val += int(c)
	return val

# this nested loop O(n^2)

def isSubset(L1, L2):
	for el in L1:
		matched = False
		for e2 im L2:
			if el == e2:
				matched = True
				break
		if not matched:
			return False
	return True
	
#len(L1)* len(L2) and O(n^2)
def intersect(L1, L2):
	tmp = []
	for e1 in L1:
		for e2 in L2:
			if e1 == e2:
				tmp.append(e1)
	res = []
	for e in tmp:
		if not(e in res):
			res.append(e)
	return res
	

	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
