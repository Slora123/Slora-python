N = 7
M = 21
for i in range(1, N, 2):
    pattern = ".|."*i
    print(pattern.center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N-2, -1, -2):
    pattern = ".|."*i
    print(pattern.center(M,"-"))

    
    
   