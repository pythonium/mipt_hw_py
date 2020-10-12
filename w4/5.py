def even(arr):
	s = 0
	for i in arr:
		if i % 2 == 0:
			s += 1
	return s


def dec(f):
	def wrapper(arr):
		s = even(arr)
		if s == 0:
			return("нет")
		elif s > 10:
			return("очень много")
		else:
			return s
	return wrapper

neweven = dec(even)

a = [i for i in range(100)] # >10 четных
b = [1, 3]                  #нет четных
c = [i for i in range(10)]  #не много четных

print("even(a) = ", even(a), " neweven(a) = ", neweven(a))
print("even(b) = ", even(b), " neweven(b) = ", neweven(b))
print("even(c) = ", even(c), " neweven(c) = ", neweven(c))
