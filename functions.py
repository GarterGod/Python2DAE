def read():
    filetoreadfrom=open("notouch.txt","r")
    line=filetoreadfrom.readline().rstrip("\n")
    while line !="":
        print(line)
        line=filetoreadfrom.readline().rstrip("\n")
def clear():
    filetowriteto=open("notouch.txt", "w")
    filetowriteto.write("")
    print("Cleared")
def write():
    filetowriteto=open("notouch.txt", "a")

    filetowriteto.write(input("input: "))
    filetowriteto.write("\n")
def BallFinder (Net): 
    import random
    global Ball
    Ballmin=0
    Ballmax=0
    while Ballmin==Ballmax:
      
        Roll()
        Ballmin=waw
        Roll()
        Ballmax=waw
    Ball=Net

    while Ball==Net:
        if Ballmin>Ballmax: 
            random_numbers = random.randint(Ballmax,Ballmin) 
            Ball=random_numbers

        elif Ballmax>Ballmin:
            random_numbers = random.randint(Ballmin,Ballmax) 
            Ball=random_numbers   
def Adding(waw,Ball):
  
    Roll()
    if waw<0:
        Ball=Ball+waw
        waw=waw*-1
        print(f"Subtracting {waw}")
        print()
        print(Ball)
        print()
       
    else:
        print(f"Adding {waw}")
        Ball=Ball+waw
        print()
        print(Ball)
        print()
def Roll(Minumum, Maximum):
    global waw
    import random
    random_number=random.randint(Minumum, Maximum) 
    waw = random_number   
def Subtracting(waw,Ball):

    if waw<0:
        Ball=Ball-waw
        waw=waw*-1
        print(f"Adding {waw}")
        print()
        print(Ball)
        print()
        
    else:
        print(f"Subtracting {waw}")
        Ball=Ball-waw
        print()
        print(Ball)
        print()      





