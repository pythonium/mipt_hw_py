
def a():
	print("This is function a")
def b():
	print("This is function b")
def c():
	raise ValueError('my exception')
	print("This is function c")
a()
b()
c()
