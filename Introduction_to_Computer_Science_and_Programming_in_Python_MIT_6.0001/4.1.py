
# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\4.1.py



# def is_even(i):
	# """
	# input: i, a positive int
	# Returns True if i is even, otherwise False
	# """
	
	# print("inside is even")
	# return i%2 == 0

	
# is_even(3)



# def if_is_even(i):
	# """
	# input: i, a positive int
	# Returns True if i is even, otherwise False
	# """
	# if i%2 == 0:
		# print("inside is even")
		# return i%2 == 0
	# else:
		# print("inside is odd")
		# return i%2 == 1
		
		
		
# if_is_even(3)


# def is_even_with_return(i):
	# """
	# input: i, a positive int
	# Returns True if i is even, otherwise False
	# """
	# print("with return")
	# remainder = i % 2
	# return remainder == 0

# #is_even_with_return(3)
# print(is_even_with_return(3))



# def is_even_without_return(i):
	# """
	# input: i, a positive int
	# Returns True if i is even, otherwise False
	# """
	# print("without return")
	# remainder = i % 2
	# #return None


# #is_even_without_return(3)
# print(is_even_without_return(3))

# def is_even(i):
	# """
	# İnputs positive int
	# Returns Boolean
	# """
	# remainder = i % 2
	# return remainder == 0



# print("All numbers between 0 and 20: even or not")

# for i in range(20):
	# if is_even(i):
		# print(i, "even")
	# else:
		# print(i, "odd")

# def func_a():
	# print("inside func_a")
	# #returns None -- important
# def func_b(y):
	# print("inside func_b")
	# return y
# def func_c(z):
	# print("inside func_c")
	# return z()

# print(func_a())
# print(5+func_b(2))
# print(func_c(func_a))


# def f(x):
	# x = 1
	# x += 1
	# print(x)

# x = 5
# f(x)
# print(x)


# def g(x):
		# print(x)
		# print(x+1)
		
# def h(x):
	# x += 1

# x = 5
# h(x)
# print(x)


def g(x):
	def h():
		x = "abc"
	x = x + 1
	print("g: x=", x)
	h()
	return x

	
x = 3
z = g(x)





























