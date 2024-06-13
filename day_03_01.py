#conditional statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("Congrats,you can ride the rollercoaster")
  age=int(input("What is your age?"))
  if age <12:
    print("Childs tickets are 12 dollar")
    bill = 12
  elif age <=18:
    print("Youths tickets are 14 dollar")
    bill = 14
  elif age>18:
    print("Adult tickets are 16 dollar")
    bill = 16

  boolean=input("Do you want a photo? Yes or No  ")
  if boolean == "Yes":
    bill= bill+3
    print(f"Your total bill is {bill}")
  if boolean == "No":
    print(f"Your total bill is {bill}")


else:
  print("Sorry, you are not tall enought to ride this rollercoaster.May be try in kid section xD")

#to check the equality we use double equal sign (==)
# to assign value we use one equal sign(=)
#we can also use greater than equal (>=) or less than equal (<=)

#even odd
# Which number do you want to check?
number = int(input())

x= int(number)%2

if x == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


#bmi calculator

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi = weight/height**2

if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif  25 <= bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif  30 <= bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


#checking leap year
year = int(input())

if year%4==0:
  if year%100 ==0:
    if year%400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")

else:
  print("Not leap year")



#love calculator 
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

new = name1+name2
x=0
new = new.lower()
x=new.count("t")
x= x + new.count("r")
x= x+ new.count("u")
x = x + new.count("e")

y=0
y=new.count("l")
y=  y + new.count("o")
y=  y + new.count("v")
y = y + new.count("e")

score = x*10 + y

if int(score)<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif int(score)>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")




#pizza order service

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0
if size =="S":
  bill = 15
  if add_pepperoni == "Y":
    bill = bill+2
if size =="M":
  bill = 20
  if add_pepperoni == "Y":
    bill = bill+3
if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill = bill+3
if extra_cheese == "Y":
  bill = bill+1

print(f"Your final bill is: ${bill}.")


