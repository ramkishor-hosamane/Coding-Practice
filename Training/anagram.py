def is_anagram(s1,s2):
	if len(s1)!=len(s2):
		return "NA"
	h1 = {}
	h2 = {}
	for x in s1:
		if not h1.get(x):
			h1[x]=1
		else:
			h1[x]+=1

	for x in s2:
		if not h2.get(x):
			h2[x]=1
		else:
			h2[x]+=1

	for x in h1:
		if h2.get(x) != h1[x]:
			return ("NA")
	return "A"


#s1 = input("Enter string 1")
#s2 = input("Enter string 2")
s1 = "ammns"
s2 = "mamn"

print(is_anagram(s1,s2))