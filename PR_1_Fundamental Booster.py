print("Welcome to the Interactive Personal Data Collector!")
print()
name=str(input("Enter your name :-"))
age=int(input("Enter Your Age :-"))
height=float(input("Enter your height in cm:-"))
favouritenum=int(input("Enter your Favourite number:-"))

print()
print("Thank you! Here is the information collected :")
print()
print("name:-", name, " (type:", type(name)," Memory address:",id(name),")")
print("age:-", age, "(type:", type(age),"Memory address:",id(age),")")
print("height:-", height, "(type:", type(height),"Memory address:",id(height),")")
print("favnum:-", favouritenum, "(type:", type(favouritenum),"Memory address:",id(favouritenum),")")
print()

currentyear = 2025
bornyear = currentyear-age
print("your birth year is approximately.:",bornyear,"(based on your age of",age,")")
print()
print("Thank you for using the personal data collector. Goodbye !")

