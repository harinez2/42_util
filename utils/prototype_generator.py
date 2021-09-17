import os
import re

path = os.path.dirname(__file__) + '/../srcs'
prototype_h = os.path.dirname(__file__) +'/../inc/prototypes.h'
indentlv = 3

files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[-1] == ".c"]

l = list()
for file in files_file:
	with open(path + '/' + file) as f:
		l.append('// ' + file)
		l_strip = [s.rstrip() for s in f.readlines()]
		flg = 0
		for s in l_strip:
			if flg == 1:
				l.append(s + ';')
				flg = 0
				continue
			if re.fullmatch('^[vitcs][^t].*\)', s):
				l.append(s + ';')
			if re.fullmatch('^[vitcs][^t].*[^\)]', s):
				l.append(s)
				flg = 1

l2 = list()
for line in l:
	m = re.match(r'([a-z_]+)(\t+)(.*)', line)
	if m != None:
		currenttabcnt = len(m.group(1)) // 4 + len(m.group(2))
		extratabcnt = indentlv - currenttabcnt
		l2.append(m.group(1) + m.group(2) + '\t' * extratabcnt + m.group(3))
	else:
		m = re.match(r'\t+(.*)', line)
		if m != None:
			extratabcnt = indentlv + 1
			l2.append('\t' * extratabcnt + m.group(1))
		else:
			l2.append(line)

with open(prototype_h, mode='w') as f:
	f.write('#ifndef PROTOTYPES_H\n')
	f.write('# define PROTOTYPES_H\n')
	f.write('\n')
	for line in l2:
		f.write(line + '\n')
	f.write('\n')
	f.write('#endif\n')

print(prototype_h + ' is updated.\n')
