def importSource(importFile):
	with open(importFile) as file:
		global deities
		deities = []
		for line in file:
			if line[0] != '#' and line[0] != '\t':
				deities.append(line.strip('\n'))
		for i in range(len(deities)):
			deities[i] = deities[i].split('\t')
			w = len(deities[i])
			j=0
			while j < w:
				if deities[i][j] == '':
					deities[i].pop(j)
					w = w-1
				else:
					j = j+1
		k=0
		r=len(deities)
		while k < r:
			if deities[k] == []:
				deities.pop(k)
				r=r-1
			else:
				k=k+1
	result = {}
	for item in deities:
		result.setdefault(item[0], {}).update({item[1]: item[2]})
	print(result)
importSource('/home/mrtreev/Documents/School/Year12/12SOFDEV/ProjectWyrmwraith/Development/Source/pathfinder/paizo/roleplaying_game/core_rulebook/cr_deities.lst')