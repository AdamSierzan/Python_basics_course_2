x = 3*4.4234353
print(round(x, 7))
print()
print("Who's that?"" " + "\nThat's 'Adam', \tsaid Juliet.")
weight = 67
haight  = 1.79
bmi  = weight / haight**2
print(bmi) 
print(round(bmi, 2))

print("{:f}".format(bmi)) 
print("%f." %bmi)

# aby zaokrąglić
print("{:.2f}".format(bmi))
print("%.2f." %bmi)

print()
#calories needed
weight_2 = 63
haight_2 = 170
age = 25
S = -161
# consistency = 
ppm =  ( 10*weight_2 ) + ( 6.25*haight_2 ) - ( 5*age ) + S 
print(ppm*1.6)