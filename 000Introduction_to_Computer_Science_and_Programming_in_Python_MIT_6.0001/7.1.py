
# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\7.1.py

# try:
	# a = int(input("tell me one number: "))
	# b = int(input("tell me another number: "))
	# print(a/b)
# except:
	# print("bug in user input")
	
	
# try:
	# a = int(input("tell me one number: "))
	# b = int(input("tell me another number: "))
	# print("a/b = ", a/b)
	# print("a+b = ", a+b)
	
# except ValueError:
	# print("Could not convert to a number.")
	
# except ZeroDivisionError:
	# print("Cant divide by zero")
	
# except:
	# print("Something went very wrong")
	


	
def get_ratios(L1, L2):
	ratios = []
	for index in range(len(L1)):
		try:
			ratios.append(L1(index)/L2(index))
		except ZeroDivisionError:
			ratios.append(float("nan")) # nan = not a number
		except:
			raise ValueError("get_ratios called with bad arg")
	return ratios
	
	
L1 = [10,20,30,40,50]
L2 = [1,2,3,4,5]	
x = get_ratios(L1/L2)

print(x)	



