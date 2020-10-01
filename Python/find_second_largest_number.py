def countOccOfEachCharacter(s):
    count = [0]*26
    
    for i in s:
        count[ord(i)-97]+=1 
    
    #print count of each chracter 
    for j in s:
        print(str(j)+":"+str(count[ord(j)-97]))
    
try:
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    arr = list(set(arr))
    arr.sort(reverse=True)
    if len(arr)>=2:
        print("The second largest number in given collection is: "+str(arr[1]))
    else:
        print("Only one number i.e "+str(arr[0])+" present in the collection.")
except:
    pass
