import os
dirPath = r"C:\\Users\\tjen\\Desktop\\Python"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
with open('list.csv', 'w', encoding ='UTF-8') as f:
	f.write('File Name, File Type\n')
	for l in result:
		if '.JPG' in l:
			n,b =str(l).split('.')
			f.write(n +','+ b + '\n')