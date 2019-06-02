# s = "abcdefgh"

# print(s[3:6])

# print(s[::-1])

#strings are immutable - cannot be modified



# s = "hello"

# s[0]

# s = "y" + s[1:len(s)]

# print(s)


# s = "abcdiefguhu"
# for index in range(len(s)):
	# if s[index] == "i" or s[index] == "u":
		# print("There is an i or u")
		

# for char in s:
	# if char =="i" or char =="u":
		# print("There is an i or u")
	

	
	
	
# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
	# char = word[i]
	# if char == " ":
		# pass
	# elif char in an_letters:
		# print("Give me an " + char + "!" + char)
	# else:
		# print("Give me a " + char + "!" + char)
	# i += 1
# print("What does that spell?")
# for i in range(times):
	# print(word, "!!!")
	
	
	
# i = 0
# for char in word:
	# if char == " ":
		# pass
	# elif char in an_letters:
		# print("Give me an " + char + "!" + char)
	# else:
		# print("Give me a " + char + "!" + char)
# print("What does that spell?")
# for i in range(times):
	# print(word, "!!!")

# cube = 8

# for guess in range(abs(cube+1)):
	# if guess**3 >= abs(cube):
		# break
	# if guess**3 != abs(cube):
		# print(cube, "is not a perfect cube")
	# else:
		# if cube < 0:
			# guess = -guess
			
		# print("Cube root of", str(cube), "is", str(guess))
		

#aprox solutions

# cube = 10000
# epsilon = 0.01
# guess = 0.0
# increment = 0.00001
# num_guesses = 0
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
	# guess += increment
	# num_guesses += 1
# print("num_guesses= ", num_guesses)
# if abs(guess**3 - cube) >= epsilon:
	# print("Failed on cube root of", cube)
# else:
	# print(guess, "is close to the cube root of", cube)
		


cube = 27
epsilon = 0.01
num_guesses = 0
low = 0.0
high  = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
	if guess**3 < cube:
		low = guess
	else:
		high = guess
	guess = (high + low)/2.0
	num_guesses += 1
print("num_guesses= ", num_guesses)


if abs(guess**3 - cube) >= epsilon:
	print("Failed on cube root of", cube)
else:
	print(guess, "is close to the cube root of", cube)
		
		
		
		

		

