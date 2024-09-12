#print ("hello world")
#02 legal variable are 7 
#myname = "nadia "
#print (myname) 
#name = "nadia"
#print (name )
#snake case writing 
#_name = "nadia "
#print(_name ) 
#camel case writing 
#nameFirst = "nadia "
#print (nameFirst)
#pascal case writing 
#NameFirst = "nadia "

#print (NameFirst)

#03 illegal variable
#1name = "nadia "
#print (name)

#hypenated wrting style
#name_name = "nadia "
#print (name_name)

#04 variable string 

#name = "nadia "
#age = 22

#print(f"my name is {name} and my age is {age}")
#print (name,age)

#05 maths ambiguity 
#a=2+3*5
#print (a)

#06 condition 
#x=11
#if x==10:
#print ("x is 10")
#else:
#print ("x is not 10")

# condition 

#hp=10
#if (hp>=10):
#print ("hp is)
      #else:
   # print("you do not have enough health points")

#hp=10
#if(hp!=10):
#print("you have enough health points")

#else:
#print("you do not have enough health points")

    #07 input 
    #name = input("Enter your name: ")
    #print("Hello", name)

#task 
#e=int(input("enter your education: "))
#a=int(input("enter your age "))
#h=int(input("enter your height"))


#if (e>14 and a>18 or h>5):
#print ("you are eligible for work ")
#else:
#print ("you are not eligible  for work ")


#task 21 august 
#assignment no 3
#tuple 
#tup=(1,2,3,4,5)
#print(tup)
#print("type(tup)")

#1:
#tub=( "1,2,3,4,5 ,"" nadia" )
#print(tub)

#2
#tup=( "1,2,3,4,5,")
#y=list(tup)
 #y.append("nadia ")
#s="a"
#print(y)

#3
#tub=("1,2,3,4 ,5")
# y=list(tub)
# y.insert(3,"nadia")
# print(y)

#4
#tub=("1,2,3,4,5")
#y=list(tub)
#y.insert(0,"nadia ")    
#print(y)

#class objects 

#class person :
  #x=10**2

#p= person ( )

#print(p.x)

#class person

#def __init__(self,name,age):
    #self.name =name
    #self.age = age
#def show(self):
    #print (f"name, {self.Name} ,age:{self.age}") 



 #assignment 2 

#num = input ("enter your number" )

#print ("my number is" , 3)

# Get the number from the user
#num = int(input("Enter a number: "))

# Print the multiplication table up to 10
#for j in range(1, 11):
   # print(num, 'x', j, '=', num * j)

#assignment 6

# Function to perform the desired operation
def calculator():
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Take input from the user for the operation
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Validate input
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation selection.")
        return
    
    # Take input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform the chosen operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division is: {result}")

# Run the calculator function
#calculator()




name = "nadia "
age = "18 "
#print("my name is " + name +" + age")

num = input("Enter your number: ")
num = int(num)
print (type(num))






































































