def calHCF(a,b):
    return b if a%b==0 else calHCF(b, a%b)

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().split()))
    hcf = calHCF(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        hcf = calHCF(hcf, arr[i])
    
    print(hcf)
