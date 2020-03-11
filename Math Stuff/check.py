def remove_duplicate(arr):
    nd,ndn=[],[]
    for i in arr:
        for x,y in i.items():
            if y not in nd:
                nd.append(y)
                ndn.append(i)
    return ndn

def remove_duplicate(arr)
    return set([  v1   for k1,v1 in v.items() for k,v in i.items() for i in arr])