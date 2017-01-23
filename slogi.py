from katakana import *
from hiragana import *
from other import *
def slogi(slovo, sl, romaji_k, romaji_h, az):
    s=[]
    g=[]
    u=[]
    r=[]
    k=[]
    ind=0
    flag=0
    slovo=slovo+" "
    for p in slovo:
        if p=='k' or p=='s' or p=='t' or p=='n' or p=='h' or p=='m' or p=='r' or p=='w' or p=='g' or p=='z' or p=='d' or p=='b' or p=='p' or p=='c' or p=='y' or p=='j' or p==" ":
            if flag==1:
                u.append(s)
                if az==1:
                    k.append(katakana(s, sl, romaji_k))
                if az==2:
                    k.append(hiragana(s, sl, romaji_h))
                s=[]
                flag=0
                ind=0
            s.append(p)
            ind=ind+1
            if p=='n':
                flag=1
        else:
            if ind==1:
                r=add_2(s[0],p)
            if ind==2:
                r=add_3(s[0],s[1],p)
            if ind!=0:
                for t in sl:
                    for y in r:
                       if y==t:
                            u.append(r)
                            if az==1:
                                k.append(katakana(r, sl, romaji_k))
                            if az==2:
                                k.append(hiragana(r, sl, romaji_h))
                            r=[]
                            ind=0
                            s=[]
                            flag=0                            
                            break            
            else:                 
                r.append(p)
                for t in sl:
                     for y in r:
                        if y==t:
                            u.append(p)
                            if az==1:
                                k.append(katakana(p, sl, romaji_k))
                            if az==2:
                                k.append(hiragana(p, sl, romaji_h))
                            s=[]
                            r=[]
                            ind=0
                            break
    print(u)
    print(k)
