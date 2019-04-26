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
	

	
	
	
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
	char = word[i]
	if char == " ":
		pass
	elif char in an_letters:
		print("Give me an " + char + "!" + char)
	else:
		print("Give me a " + char + "!" + char)
	i += 1
print("What does that spell?")
for i in range(times):
	print(word, "!!!")
	
	
	
	
