#from slovar import *
def transl(word, sl, t):
	ind=0
	for k in sl:
		ind = ind+1
		if word==sl:
			return t[ind]