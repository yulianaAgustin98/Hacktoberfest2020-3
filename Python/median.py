import random
def med(l):
    if(len(l) % 2):
        return give(l,len(l)//2)
    else:
        return  (give(l,len(l)//2) + give(l,len(l) // 2 + 1) )/ 2





def give(l,k):
    pivot = l[0]
    lows = [i for i in l if i < pivot]
    highs = [i for i in l if i > pivot]
    pivots = [i for i in l if i == pivot]

    if(k  < len(lows)):
        return give(lows,k)
    elif( k < len(lows) + len(pivots)):
        return pivots[0]
    else:
        return give(highs,k - len(lows))


l = [10,20,30,40]
print(med(l))