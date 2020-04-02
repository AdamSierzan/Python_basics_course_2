print("How old are you:")

age  = int(input())
responsible = input("Are you responsible:? T/N")
if (age > 100):
    print("You're definetly an adult")
elif (age > 18) and responsible == "T":
    print("You're a responsible adult")
elif responsible != "T":
    print("You're unresponsible adult")
else:
    print("You're not an adult")