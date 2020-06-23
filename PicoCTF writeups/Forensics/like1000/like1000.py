import tarfile
for i in range(1000, 0, -1):
	tar = tarfile.open(str(i) +  ".tar")
	print("extracting " + str(i))
	tar.extractall("./")
	tar.close()
