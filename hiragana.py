from katakana import *
from slogi import *
from other import *
def hiragana(u, sl, romaji_hir):
    s=[]
    ind=0   
    for t in sl:
         for y in u:
             ind=ind+1            
             if y==t:                
                 s.append(romaji_hir[ind-1])
                 ind=0
                 break
    return s