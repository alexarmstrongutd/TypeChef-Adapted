
with open('headerLocations.txt', 'r') as header:
	lines = header.readlines()
	fileSet = set()
	for line in lines:
		line = line.strip()
		fileSet.add(line)
	fileList = list(fileSet)
	with open('headerSet.txt','w+') as newFile:
		for x in fileList:
			newFile.write(x + '\n')
