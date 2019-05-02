


import one

print("Top level in tow.py")

one.func()

if __name__ == "__main__":
	print("two.py is being run directly")
else:
	print("two.py imported")