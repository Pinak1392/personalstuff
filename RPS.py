import random
choices = ["R","P","S"]

def checkVictory(a,b,c):
	if(c!=b and (b == a or c == a) and a == "P"):
		return 1
	if(c==b and (a!=b and a!=c) and a == "R"):
		return 1
	if((a != b and b!=c and c!=a) or (a==b and c==b) and a == "S"):
		return 1
	
	return 0

def rockPaperVictory(a,b):
	if((b == "P" and a=="S") or (b == "S" and a=="R") or (b == "R" and a=="P")):
		return 1
	return 0


testVaryRange = []
for h in range(1000):
	scores = [0 for i in range(4)]
	for i in range(100):
		players = [random.choice(choices) for i in scores]
		for i in range(len(players)):
			scores[i] += checkVictory(players[i], players[(i+1)%len(players)], players[(i-1)%len(players)])

	var = [(i - sum(scores)/len(scores))**2 for i in scores]
	testVaryRange.append((sum(var)/len(scores))**(1/2))

print(sum(testVaryRange)/len(testVaryRange))

testVaryRange = []
for h in range(1000):
	scores = [0 for i in range(2)]
	for i in range(100):
		players = [random.choice(choices) for i in scores]
		for i in range(len(players)):
			scores[i] += rockPaperVictory(players[i], players[(i+1)%len(players)])

	var = [(i - sum(scores)/len(scores))**2 for i in scores]
	testVaryRange.append((sum(var)/len(scores))**(1/2))

print(sum(testVaryRange)/len(testVaryRange))
