

# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\6.1.py


# MUKTIPLICATION - ITERATIVE SOLUTION

# def mult_iter(a, b):
	# result = 0
	# while b > 0:
		# result += a
		# b -= 1
	# return result

	
# print(mult_iter(3,6))



# MULTIPLICATION - RECURSIVE SOLUTION

# def mult(a, b):
	# if b == 1:
		
		# return a
	# else:
		
		# return a + mult(a, b-1)


# print(mult(5, 10))


# FAACTORIAL - RECURSEIVE

# def fact(n):
	# if n == 1:
		# return 1
	# else:
		# return n*fact(n-1)
		
# print(fact(4))


# FACTORIAL - ITERATIVE

# def factorial_iter(n):
	# prod = 1
	# for i in range(1, n+1):
		# prod *= i 
	# return prod
	


# print(factorial_iter(4))



# def printMove(fr, to):
	# print("move from " + str(fr) + " to " + str(to))

# def Towers(n, fr, to, spare):
	# if n == 1:
		# printMove(fr, to)
	# else:
		# Towers(n-1, fr, spare, to)
		# Towers(1, fr, to, spare)
		# Towers(n-1, spare, to, fr)
		
# def fib(x):
	# """
	# assumes x an int >= 0
	# returns fibonacci of x
	# """

	# if x == 0 or x ==1:
		# return 1
	# else:
		# return fib(x-1) + fib(x-2)
		
	


# print(fib(4))

# def isPalindrome(s):
	
	# def toChars(s):
		# s= s.lower()
		# ans = ""
		# for c in s:
			# if c in "abcdefghijklmnıpqrstuvwxyz":
				# ans = ans + c
		# return ans
	# def isPal(s):
		# if len(s) <= 1:
			# return True
		# else:
			# return s[0] == s[-1] and isPal(s[1:-1])
	# return isPal(toChars(s))
	
# print(isPalindrome("abbccccbbaa"))

# names = ["Ana", "John", "Denise", "Katy"]

# grade = ["B", "A+", "A", "A"]

# course = [2.00, 6.0001, 20.002, 9.01]

# def get_grade(student, name_list, grade_list, course_list):
	# i = name_list.index(student)
	# grade = grade_list[i]
	# course = course_list[i]
	# return(course, grade)

	

# my_dict = {}
# grades = {"ana":"b", "john":"a+", "denise":"a", "katy":"a"}

# grades["ana"]
# grades["sylvan"]

# # Add an entry

# grades["sylvan"] = "A"

# test if key in dictionary

# "john" in grades
# "daniel" in grades
 
# # Delete entry

# del(grades["Ana"])

# returns keys

# grades.keys()

# returns values

# grades.values()


# def lyrics_to_frequencies(lyrics):
	# myDict = {}
	# for word in lyrics:
		# if word in myDict:
			# myDict[word] +=1
		# else:
			# myDict[word] = 1
	
	# return myDict

# she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
# 'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

# 'you', 'think', "you've", 'lost', 'your', 'love',
# 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
# "it's", 'you', "she's", 'thinking', 'of',
# 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

# 'she', 'says', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'she', 'said', 'you', 'hurt', 'her', 'so',
# 'she', 'almost', 'lost', 'her', 'mind',
# 'and', 'now', 'she', 'says', 'she', 'knows',
# "you're", 'not', 'the', 'hurting', 'kind',

# 'she', 'says', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',

# 'you', 'know', "it's", 'up', 'to', 'you',
# 'i', 'think', "it's", 'only', 'fair',
# 'pride', 'can', 'hurt', 'you', 'too',
# 'pologize', 'to', 'her',

# 'Because', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'Yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'yeah', 'yeah', 'yeah',
# 'yeah', 'yeah', 'yeah', 'yeah'
# ]

# beatles = lyrics_to_frequencies(she_loves_you)

# print(beatles)


def most_common_words(freqs):
	values = freqs.values()
	best = max(values)
	words = []
	
	for k in freqs:
		in freqs[k] == best:
			words.append(k)
	
	return(words, best)
	


def words_often(freqs, minTimes):
	result = []
	done = False
	while not done:
		temp = most_common_words(freqs):
		if temp[1] >= minTimes:
			result.append(temp)
			for w in temp[0]:
				del(freqs[W])
		else:
			done = True

print(words_often(beatles, 5))
	


# fibonacci with dictionary more efficient way

def fib_efficient(n, d)
	if n in d:
		return d[n]
	else:
		ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
		d[n] = ans
		return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))














