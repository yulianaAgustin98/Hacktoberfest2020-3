  def Display():
    print("   0  1  2")
    for i,Row in enumerate(Game):    
        print(i,Row)

Game = [[0,0,0],[0,0,0],[0,0,0]]
Display()

print("Enter Row Number")
a=input()
print("Enter Column Number")
b=input()

Game[int(a)][int(b)]=1
Display()
