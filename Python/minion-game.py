s = input()
st,kv = 0,0
v = ['A','E','I','O','U']
for i in range(len(s)):
    if (s[i] not in v):
        st += (len(s) - i)

    elif (s[i] in v):
        kv += (len(s) - i)

if(st > kv):
    print("Stuart", st)
elif(st < kv):
    print("Kevin", kv)
else:
    print("Draw")
