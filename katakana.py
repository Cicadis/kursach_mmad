from hiragana import *
from slogi import *
from other import *
def katakana(u, sl, romaji_kat):
    s=[]
    ind=0   
    for t in sl:
         for y in u:
             ind=ind+1            
             if y==t:                
                 s.append(romaji_kat[ind-1])
                 ind=0
                 break
    return s