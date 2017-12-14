import os
'''
Purpose: to test if an object contains an item
'''
def containsItem(thing, item):
	h = 0
	for i in range(len(thing)):
		if thing[i] == item:
			h = 1
	str(thing)
	return h



'''
Purpose: to convert a .lst source file into a python dictionary
'''
def importSource(importFile):
	with open(importFile) as file:
		source = {}
		for line in file:
			if line[0] != '#' and line[0] != '\t' and line[0] != '\n' and ("SOURCELONG:" not in line):
				stats = line.split('\t')[1::]
				w = len(stats)
				j=0
				while j < w:
					if stats[j] == '':
						stats.pop(j)
						w = w-1
					else:
						stats[j] = stats[j].strip('\n')
						if containsItem(stats[j], '|') == 1:
							stats[j] = stats[j].split('|')
							for i in range(len(stats[j])):
								stats.append(stats[j][i])
							stats.pop(j)
							j=j-1
						j = j+1
				source[line.partition('\t')[0]] = stats
	return source
# Debugging Stuff
'''pippi = importSource('')
bepis = list(pippi)
f = open('out.txt', 'w')
for i in range(len(pippi)):
	f.write(str(bepis[i]) + " : " + str(pippi[str(bepis[i])])+'\n')
f.close
'''
