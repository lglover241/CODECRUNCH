name = input("What is your name? ")
#Ask the name of user and assign to variable = Name
num1,num2 =input('Enter 2 numbers: ').split(" ")
#Ask the user to input 2 values and store them in variables num1 num2
#Convert the variable strings into Integers
num1 = int(num1)
num2 = int(num2)
#Add the values and store into varaible Sum
Sum = num1 + num2
#Subtract values and store into diff
diff = num1 - num2
#Multiply values and store into Mult
Mult = num1 * num2
#Divide values and store in quote
quote = num1 / num2
#Use Modulus on the values to find remainder
Mod = num1 % num2
#print results
print('Hello', name, "your results are:")
print("{} + {} = {}".format(num1,num2,Sum))
print("{} - {} = {}".format(num1,num2,diff))
print("{} * {} = {}".format(num1,num2,Mult))
print("{} / {} = {}".format(num1,num2,quote))
print("{} / {} = {}".format(num1,num2,Mod))

##Mile to KM Converter

#Ask User to input miles and assign
distance = input('Enter Distance: ')
#Convert to int
distance = int(distance)
# Ask User for distance measure and assign to measure
measure = input('Enter distance measurement: ')
#print results
if measure == "km":
    distance = distance / 1.60934
    print(name, "Your distance is ",distance, measure)
if measure == "mi":
    distance = distance * 1.60934
    print(name, "Your distance is ",distance, measure)
elif not(measure != "mi") or not(measure!= "km"):
       print(name, "You entered the wrong measure you idiot")











