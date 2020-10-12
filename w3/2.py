def write_array(array, file_name):
	array = '\n'.join(array)
	file_name.write(array)

array = ["hello", "user", "i'm", "glad", "to", "see", "you"]
with open("2.txt", "w") as file:
	write_array(array, file)
with open("2.txt", "r") as file:
	for line in file:
		print(line)

