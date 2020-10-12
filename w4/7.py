import time
from datetime import datetime
from functools import wraps

def logger(file):
	def dec(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			start = time.time()
			returned = f(*args, **kwargs)
			stop = time.time()
			timeinwork = stop - start
			start, stop = datetime.fromtimestamp(start), datetime.fromtimestamp(stop)
			returned = '-' if returned == None else returned

			with open(file, "w") as log:
				log.write(
				"called at {}\narguments: {}\nreturned: {}\nended at: {}\nexecution time:{}\n".format(start, args, returned, stop, timeinwork))

			return f(*args, **kwargs)
		return wrapper
	return dec

@logger("log.txt")
def func(a, b):
        return a + b

func(1, 2)
