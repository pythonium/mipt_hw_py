import zipfile, os
from pathlib import Path

def write_array(array, file_name):
        array = '\n'.join(array)
        file_name.write(array)

main_zip = zipfile.ZipFile("main.zip")
main_zip.extractall("main")

main_zip.close()
folder = []
for root, dirs, files in os.walk("main"):
	for file in files:
		if file.endswith(".py"):
			folders = root.split('\\')
			if folders[-1] not in folder:
				folder.append(folders[-1])
folder.sort()
with open("3.txt", "w") as file:
	write_array(folder, file)
with open("3.txt", "r") as file:
	for line in file:
		print(line)

