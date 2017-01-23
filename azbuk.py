def azb(s, t_a):
    ind =0
    b=0
    r=[]
    dls=[]
    di=0
    dla=[]
    dj=0
    ind_r=0
    dr=0
    indv=[]
    bv=0
    for u in s:
        di=di+1
    dls.append(di)
    for k in t_a:
        p=list(k)
        for t in p:
            for y in s:
                b=b+1
                if p.count(y)>=1:
                    ind=ind+p.count(y)
        for u in p:
            dj=dj+1
        dla.append(dj)
        dj=0
        if  (ind/b)>=0.75 and (ind/b)<=1:
            r.append(1)
        else:
            r.append(0)
        ind=0
        b=0
    #print(r)
    
    for o in r:
        dr=dr+1
    for o in r:
        if o==1:
            #print(t_a[ind_r])
            if dla[ind_r]==dls[0] or dla[ind_r]==(dls[0]+1) :
                #print("katakana")
                return 1
        if o==dr:
           # print("hirogana")
            return 2
        ind_r=ind_r+1
   # print("hirogana")
    return 2
