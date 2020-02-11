


#if __name__  = __main__
# python one.py

# print("hello")


# if __name__ == "__main__":
	

def func():
	print("Func() in one.py")

print("top level in one.py")

if __name__ == "__main__":
	print("one.py is being run directly")
else:
	print("not run directly, has been imported")

	
