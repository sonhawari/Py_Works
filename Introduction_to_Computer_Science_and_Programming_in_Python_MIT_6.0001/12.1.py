##
# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\12.1.py


import random
# unsorted linear search

# def linear_search(L, e):
	# found = False
	# for i in range(len(L))
		# if e == L[i]:
			# found = True
	# return found
	
# # sorted linear search

# def search(L, e):
	# for i in range(len(L)):
		# if L[i] == e:
			# return True
		# if L[i] > e:
			# return False
	# return False
	
	
# # Bisection search

# def bisect_search2(L, e):
	# def bisect_search_helper(L, e, low, high):
		# if high == low:
			# return L[low] == e
		# mid = (low + high)//2
		# if L[mid] == e:
			# return True
		# elif L[mid] > e:
			# if low == mid: # nothing left to search
				# return False
			# else:
				# return bisect_search_helper(L, e, low, mid -1)
		# else:
			# return bisect_search_helper(L, e, mid+1, high)
	# if len(L) == 0 :
		# return False
	# else:
		# return bisect_search_helper(L, e, 0, len(L) -1)

		
		
# def bogo_sort(L):
	# while not is_sorted(L):
		# random.shuffle(L)

# def buble_sort(L):
	# swap = False
	# while not swap:
		# swap = True
		# for j in range(1,len(L)):
			# if L[j-1] > L[j]:
				# swap = False
				# temp = L[j]
				# L[j] = L[j-1]
				# L[j-1] = temp

				
				
				
				
# testList = [1,3,5,7,2,6,25,18,13]
       
# print('')
# print(selection_sort(testList))
# print(testList)





def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

		
		
		
		
		
		
def merge(left, right):
	result = []
	i,j = 0,0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
	return result

def merge_sort(L):
	print('merge sort: ' + str(L))
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L)//2
		left = merge_sort(L[:middle])
		right = merge_sort(L[middle:])
		return merge(left, right)
        
testList = [1,3,5,7,2,6,25,18,13]

#print('')
#print(merge_sort(testList))
