import os
dirPath = r"C:\\Users\\tjen\\Desktop\\Python"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
#filelist=[]
with open('list.csv', 'w') as f:
	for l in result:
		if '.JPG' in l:
			#filelist.append(l)
			f.write(l + '\n')