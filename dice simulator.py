import random
list=[1,2,3,4,5,6]
for i in range(1000):
    no=random.choice(list)
    print("Dice rolled at:-",no)
    if no ==1:
        print("[-----------]")
        print("[           ]")
        print("[     0     ]")
        print("[           ]")
        print("[-----------]")
    elif no==2:
        print("[-----------]")
        print("[ 0         ]")
        print("[           ]")
        print("[         0 ]")
        print("[-----------]")
    elif no==3:
        print("[-----------]")
        print("[ 0         ]")
        print("[     0     ]")
        print("[         0 ]")
        print("[-----------]")
    elif no==4:
        print("[-----------]")
        print("[ 0       0 ]")
        print("[           ]")
        print("[ 0       0 ]")
        print("[-----------]")
    elif no==5:
        print("[-----------]")
        print("[ 0       0 ]")
        print("[     0     ]")
        print("[ 0       0 ]")
        print("[-----------]")
    elif no==6:
        print("[-----------]")
        print("[ 0   0   0 ]")
        print("[ 0   0   0 ]")
        print("[ 0   0   0 ]")
        print("[-----------]")  
    x=input("Do u want to continue? (yes/no) :-")
    if x=="no":
        break 
          
