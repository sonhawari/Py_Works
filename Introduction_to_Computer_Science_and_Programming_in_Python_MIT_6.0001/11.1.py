##
# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\11.1.py


##Bisection search implement 1

import random


# list should be sorted to this method to work

# def bisect_search1(L, e):
	# if L == []:
		# return False
	# elif len(L) == 1:
		# return L[0] == e
	# else:
		# half = len(L)//2
		# if L[half] > e:
			# return bisect_search1( L[:half], e)
		# else:
			# return bisect_search1(L[half:], e)

			
			
			
# Z = []

# for i in  range(100):
	# Z.append(random.randint(1,50))
	

# print(sorted(Z))
	
# print(bisect_search1(sorted(Z), 49))

# testList = []
# for i in range(100):
    # testList.append(i)

# print(testList)
# print(bisect_search1(testList, 45))



def bisect_search2(L, e):
	def bisect_search_helper(L, e, low, high):
		if high == low:
			return L[low] == e
		mid = (low + high)//2
		if L[mid] == e:
			return True
		elif L[mid] > e:
			if low == mid: # nothing left to search
				return False
			else:
				return bisect_search_helper(L, e, low, mid -1)
		else:
			return bisect_search_helper(L, e, mid+1, high)
	if len(L) == 0 :
		return False
	else:
		return bisect_search_helper(L, e, 0, len(L) -1)

#log complexity

def intToStr(i):
	digits = "0123456789"
	if i == 0:
		return "0"
	result = ""
	while i > 0:
		result = digits[i%10] + result
		i = i//10
	return result
	
def fact_iter(n):
	prod = 1
	for i in range(1, n+1):
		prod *= i
	return prod

	
def fact_recur(n):
	""" assume n >=0 """
	if n<= 1:
		return 1
	else:
		return n*fact_recur(n-1)


# recursive solution

def genSubsets(L):
	res = []
	if len(L) == 0:
		return [[]] # list of empty list
	smaller = genSubsets(L[:-1]) # all subsets without last element
	extra = L[-1:] #create a list of just last element
	new = []
	for small in smaller:
		new.append(small+extra) # for all smaller solutions, add one with last element
	return smaller + new # combine those with last element and those without 
	

	
# complexity of iterative fibonacci

def fib_iter(n):
	if n == 0:
		return 0
	elif m == 1:
		return 1
	else:
		fib_i = 0
		fib_ii = 1
		for i in range(n-1):
			tmp = fib_i
			fib_i = fib_ii
			fib_ii = tmp + fib_ii
		return fib_ii














