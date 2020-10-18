class Company:
    def __init__(self):
        self.stack=[]
        self.b=[]
    def simple_ball(self,a):
        stack=self.stack
        b=self.b
        for list in a:
            for element in list:
                b.append(element)
        #print(b)
        #print(len(b))
        i=0
        length=len(b)
        while i < length:
            if b[i]=="f" or b[i]=="r":
                b.pop(i)
                length = length - 1
                continue
            i+=1
        #print(b)
        for i in range(len(b)):
            stack.append(b[i])
        print(stack.pop())
n=list(map(int,input().split()))
count=n[0]
primary_id=n[1]
a=[]
for i in range(count):
    a.append(list(map(str,input().split())))
obj=Company()
obj.simple_ball(a)
