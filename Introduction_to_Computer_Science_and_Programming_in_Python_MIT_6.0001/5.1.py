

# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\5.1.py


# temp = x
# x = y
# y = temp

# (x, y) = (y, x)

# def quaotient_and_remainder(x, y):
	# q = x // y
	# r = x % y 
	# return (q, r)

# (quot,rem) = quaotient_and_remainder(4, 5)

# print(quot)
# print(rem)


# can iterate over tuples

# def get_data(aTuple):
	# nums = ()
	# words = ()
	# for t in aTuple:
		# nums = nums + (t[0],)
		# if t[1] not in words:
			# words = words + (t[1],)
	
	# min_n = min(nums)
	# max_n = max(nums)
	# unique_words = len(words)
	# return (min_n, max_n, unique_words)

	
# test = ((1, "a"), (2, "b"),
# (1, "a"), (7, "b")
# )

# (a, b, c) = get_data(test)
# print("a:",a,"b:",b,"c:",c)

# tswift =(
# (2014, "Katty"),
# (2014, "Harry"),
# (2012, "Jake"),
# (2010, "Taylor"),
# (2008, "Joe")
# )

# (min_year, max_year, num_people) = get_data(tswift)
# print("From", min_year, "to", max_year, "Taylor swift wrote songs about", num_people, "people")



# L = [2,3,4,[1,2]]
# total = 0
# for i in range(len(L))
	# total += L[i]
# print total


# L = [5,10,15]
# total = 0
# for i in L:
	# total += i 
# print(total)


# L = [2,1,3]
# L.append(5)
# print(L)



# L1 = [2,1,3]
# L2 = [4,5,6]
# L3 = L1 +L2

# print(L3)
# L1.extend(L2)
# print(L1)

# L = [2,1,3,6,3,7,0]
# print(L)

# L.remove(2)
# print(L)

# L.remove(3)
# print(L)

# del(L[1])
# print(L)

# L.pop()
# print(L)

# s = "I<3 cs"
# list(s)
# s.split("<")
# L = ["a","b","c"]

# "".join(L)
# "_".join(L)


# L = [9,6,0,3]
# print(L)
# print(sorted(L))
# print(L)
# L.sort()
# print(L)
# L.reverse()
# print(L)

# a = 1
# b = a
# print(a)
# print(b)

# warm = ["red", "yellow", "orange"]
# hot = warm
# hot.append("pink")
# print(hot)
# print(warm)




# cool = ["blue","green","grey"]

# chill = cool[:]

# chill.append("black")
# print(chill)
# print(cool)

# warm = ["red","yellow","orange"]
# print(warm)
# sortedwarm = warm.sort()
# print(warm)
# print(sortedwarm)

# cool = ["grey","green","blue"]
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)


# warm = ["yellow","orange"]
# hot = ["red"]
# brightcolors = [warm]
# brightcolors.append(hot)
# print(brightcolors)
# hot.append("pink")
# print(hot)
# print(brightcolors)

# def remove_dups(L1, L2):
	# for e in L1:	
		# if e in L2:
			# L1.remove(e)

			
# L1= [1,2,3,4]
# L2= [1,2,5,6]

# remove_dups(L1, L2)

# print(L1)
# print(L2)




def remove_dups(L1, L2):
	L1_copy = L1[:]
	for e in L1_copy:
		if e in L2:
			L1.remove(e)

L1= [1,2,3,4]
L2= [1,2,5,6]		
	
print(L1)		
print(L2)




























































