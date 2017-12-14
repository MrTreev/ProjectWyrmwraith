'''
Purpose: to convert a .pcg character file to a python dictionary
'''
def loadChar(charfile):
	characters = []
	characterDetails = {}
	with open(charfile) as file:
		for line in file:
			if line[0] != '#' and line[0] != '\t':
				characters.append(line.strip('\n'))
	i=0
	while i < len(characters):
		characters[i] = characters[i].split('\t')
		w = len(characters[i])
		#cleaning empty entries
		j=0
		while j < w:
			if characters[i][j] == '':
				characters[i].pop(j)
				w = w-1
			else:
				j = j+1
		i = i+1
	#clear empty arrays
	k=0
	r=len(characters)
	u=0
	while u < len(characters):
		while k < r:
			if characters[k] == []:
				characters.pop(k)
				r=r-1
			else:
				k=k+1
		u = u+1
	#split at pipe
	u = 0
	while u < len(characters):
		characters[u] = characters[u][0].split('|')
		u=u+1
	i = 0
	while i < len(characters):
		j=0
		while j > len(characters[i]):
			print(characters[i][j])
			j = j+1
		i = i+1
	
	return characters
#loadChar('/home/opatterson/Documents/School/Year12/12SOFDEV/ProjectWyrmwraith/Development/Characters/ToPlay/Elmore(FemaleMage).pcg')
# Debugging Stuff (Print Dict)
pippi = loadChar('/home/opatterson/Documents/School/Year12/12SOFDEV/ProjectWyrmwraith/Development/Characters/ToPlay/Carum(All the HPs).pcg')
bepis = list(pippi)
f = open('/home/opatterson/Documents/School/Year12/12SOFDEV/ProjectWyrmwraith/Development/MainProgram/out.txt', 'w')
'''
for i in range(len(pippi)):
	f.write(str(bepis[i]) + " : " + str(pippi[str(bepis[i])])+'\n')
f.close
'''
for i in range(len(pippi)):
	f.write(str(pippi[i])+'\n')