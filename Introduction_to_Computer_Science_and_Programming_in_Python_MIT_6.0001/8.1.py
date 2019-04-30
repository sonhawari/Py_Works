# C:\Users\eiree\AppData\Local\Programs\Python\Python37-32\python.exe .\8.1.py

class Coordinate(object):
	#special method
	def __init__(self, x, y):
		self.x = x
		self.y = y
	# defining method to calculate distance between points
	def distance(self, other):
		x_diff_sq = (self.x - other.x) ** 2
		y_diff_sq = (self.y - other.y) ** 2
		return (x_diff_sq + y_diff_sq) ** 0.5
	# special method: Print rep. of this object
	def __str__(self):
		return "<"+str(self.x)+","+str(self.y)+">"
	
	def __add__(self, other):
		
		

c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
print(origin.x)

print(c.distance(origin))
# equivalent to
print(Coordinate.distance(c, origin))

print(c)
print(type(c))

print(isinstance(c, Coordinate))

