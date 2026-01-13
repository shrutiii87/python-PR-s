print("Welcome to the Pattern Generator and Number Analyser !")
print()

print("Select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Number")

a=int( input("Enter your choice:"))

while a<4:
    n=int(input("Enter the number for the pattern:"))

    if a==1:     

        for i in range(1, n):
            for j in range(i):
                print("*", end=" ")
            print()
 
    elif a==2:

        for i in range(1, n + 1):
            print(" " * (n-i) + "*" * (2*i-1))
            print()
  
    elif a==3:

        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * i)
            print()
  
    break

while a==4:

    n=int(input("Enter the start of the range:"))
    m=int(input("Enter the end of the range:"))

    for i in range(n, m + 1):
        print("Number",i,"is even"if i%2==0 else "is Odd")

    print("Sum fo all numbers from",n,"to",m,"is:",sum(range(n, m + 1)))

    break
        
        


        
        