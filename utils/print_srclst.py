import os
import re

path = os.path.dirname(__file__) + '/../srcs'
prototype_h = os.path.dirname(__file__) +'/../inc/prototypes.h'

files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]

flg = 0
for file in files_file:
	if flg  == 0:
		flg = 1
	else:
		print(' \\')
	print('\t\t\t\t$(SRC_DIR)/' + file, end='')
print()
