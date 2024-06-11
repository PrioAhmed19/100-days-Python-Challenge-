#Data Types


#strings

print("Hello")

# pullng a specific string at a certain index, keeping in mind that we start counting from 0

print("Hello Sage"[1])
print("Hello Sage"[6])
print("12345"[3])

#we can also get the last character using -1 . Like this we can get them backward
print("Hello Sage"[-1])
print("Hello Sage"[-2])


#using double quotes makes computer thinks inside them are strings although they are int
print("12345"[3])


#Intergers

print("123"+"456")  # this is string
print(123+456)   #this is an integer


#float
3.1212344

#boolean

True
False

#printing type of the variable
x='Ash'
print(type(x))

num_char = len(input("Whats ur name?"))
print(type(num_char))

#changing data types
#int to string
num_char = len(input("Whats ur name?"))

new_num_char = str(num_char)

print("Your name has "+ new_num_char+" characters")

#the differences
print(70 + float(69.69))
print(str(70)+str(69.69))


#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

x=two_digit_number[0]
y=two_digit_number[1]

output = print(int(x)+int(y))

#differnt mathematics expressions

2+3
2-3
2/3
2*3
print(2**3) # that means 2 to the power 3


#priorites while executing

#PEDMAS

#paranthesis
#exponents
#division
#multiplications
#addition
#substraction

#bmi calculator
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
#converting the inputs to floats
x= float(height)
y=float(weight)

z=int(y/(x**2))
print(z)

#float and int manipulation

print(8/3)  #it will give us a floating number
print(8//3)  #it will automatically convert it to an integer by chopping off everything after decimal point



# Using increment

score = 0

# condition

score = score+1
print (score)

#or there is another shortcut way

score = 0
score += 1
print(score)

# by this it will increase the score by 1



#different data types converting in one string using f-SyntaxWarning

score = 0
height = 69
iswinning = True

print(f"your score is {score}.your height is {height},your winning is {iswinning}")


#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x weeks left.
#Where x is replaced with the actual calculated number of weeks the input age has left until age 90.


age = input()
remaininig_age = 90 - int(age)

rem_week = remaininig_age*52

print(f"You have {rem_week} weeks left.")




#creating a tip calculator 

print("Welcome to Tip Calculator")
x=float(input("What's ur total bill?"))
y=int(input("Tip percentage?"))
z=int(input("How many people would like to share the total bill?"))

j= (y/100*x+x)/z

print(f"Each will pay {j}")






