## exercise 1 ##
eMessage="Hello World!"
id=12
a=24.4
print(eMessage)
print(id)
print(a)

## exercise 2 ##
mtnNames = ["Mount Everest", "K2", "Kangchenjuga", "Lhotse", "Makalu"]
print(mtnNames[2])

## exercise 3 ##
mtn = ("Kangchenjuga", 8586)
mtn[1]

## exercise 4 ##
aDict={}
aDict["Mary"]="chocolate"
aDict["Rodrigo"]="bubble gum"
aDict["Larry"]="gummy bears"
aDict["Mary"]
print("Mary's candy of chocie is", aDict["Mary"])

## exercise 5 ##
def BMI(height, weight):
    aBMI = weight / (height * height)
    return aBMI

BMI(1.60, 75)

## exercise 6 ##
import random
# generate a random number
n = random.random()
ni = round(n*1000.0, 0)
m = ni % 2 # Modulo (%) calculates the remainder after division.
if (m >0):
    print(str(ni) +" is an odd number.")
else:
    print(str(ni) +" is an even number.")

## exercise 7##
import random

for i in range(5):
    n = random.random() # Returns a value within the interval [0.0, 1.0).
    ni = round(n * 10000.0, 0)
    m = ni % 2.0 # Modulo (%) calculates the remainder after division.
    if (m > 0):
        print(str(ni) + " is an odd number.")
    else:
        print(str(ni) + " is an even number.")
## exercise 8##
sum = 0
for i in range(1, 101):
    sum = i+sum
print(sum)



## exercise 9 ##
temperature = 115
while temperature > 112: # first while loop code
    print(temperature)
    temperature = temperature - 1

print('The tea is cool enough.')
