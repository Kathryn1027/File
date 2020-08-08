import os
dirPath = r"C:\\Users\\tjen\\Desktop\\Python"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
with open('list.csv', 'w', encoding ='UTF-8') as f:
	f.write('File Name\n')
	for l in result:
		if '.JPG' in l:
			f.write(str(l)+ '\n')