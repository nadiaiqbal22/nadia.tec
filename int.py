#marks = int(input("enter your marks "))
#if (marks>=90 or marks<=100):
    #print("Grade: A")

#else:("Grade: B")

#pakscore = int(input("enter your score "))

#if  (pakscore <=100 or pakscore <=150):
     
   #  print("pak winner")

#elif (pakscore > 150 and pakscore <= 200):
     
    # print("pak second")

# 11 list
#name=[12]
#name=name+["nadia"]
#name.append("iqbal")
#print(type(name),name)


#sets

#set1={1,2,3,4,5}
#set2={"hello" ,"world"}

#print(set1)

#to add in set

#set1={1,2,3,4,5}
#set.add(6)
#print(set1)

#find length

#print(len(set1))

#to check index 
#print(len(set1)-1)

#update set

#set1={1,2,3,4,5}
#set2={6,7,8,9}

#set1.update(set2)
#print(set1)

#to remove set

#set1={1,2,3,4,5}
#set1.remove(2)
#print(set1)

#discard set 

#set1={1,2,3,4,5}
#set1.discard(9)

#print(set1)

#union of set 

#set1={1,2,3,4,5}
#set2={5,6,7,8,9,10}

#set3=set1.union(set2)
#print(set3)

#set3= set1 | set2
#print(set3)

#intersection of set

#set1={1,2,3,4,5}
#set2={5,6,7,8,9,10}

#set3=set1.intersection(set2)

#print(set3)

#set3=set1&set2

#print(set3)

#to find difference


#pt = input("enter your name : ")

#print(pt)
#print(type(pt))

#21 iteration and iterables

# ls=[1,2,3,4,5,6,7,8]
# ls2=iter(ls)
# print(next(ls2))

#22 function and variable scope 
#1:
#def s():
 #print ("hello world")

#s()

#2:
#def s():
  #return ("hello world")

#print(s( )) 

#3  
#def s():
    #return ("hello world")

#p=s()
#print(p)

#4:

#def sum (p,s):
#print("hello world",p+s)
#sum(89,91)

#5

#sum(p,s)


print ("welcome to my car showroom")
credit = int(input("enter your budget"))
print("""
        choice your option
        1 if you want to buy car then go to counter A 
        2 if you want to rent a car than go to counter B
        3 if you are just visiting showroom than go to counter C
        4 if you want to leave than exit is next to counter A""")
      
user_choice = int(input("enter your option"))


if user_choice == 1:
 print("""welcome sir!
          choice your car
            1. Honda City
            2. Toyota Corolla
            3. BMW X5
            4. Mercedes-Benz E-Class
            5. SUV""")
 car_choice = int(input("enter your car choice"))
 if car_choice == 1:
  if credit >= 3000000:
   print("your car is selected")
   print("your car is Honda City")
   print("your car cost is 3000000")
   print("thank you for visiting my showroom")
  else:
   print("your budget is not sufficient")
 if car_choice == 2:
  if credit >= 2500000:
   print("your car is selected")
   print("your car is Toyota Corolla")
   print("your car cost is 2500000")
   print("thank you for visiting my showroom")
  else:
   print("your budget is not sufficient")
if car_choice == 3:
  if credit >= 6845000:
   print("your car is selected")
   print("your car is BMW X5")
   print("your car cost is 6845000")
   print("thank you for visiting my showroom")
  else:
   print("your budget is not sufficient")
if car_choice == 4 :
 if credit >= 7050000:
  print("your car is selected")
  print("your car is Mercedes-Benz E-Class")
  print("your car cost is 7050000")
  print("thank you for visiting my showroom")
if car_choice == 5:
 if credit >= 5500000:
  print("your car is selected")
  print("your car is SUV")
  print("your car cost is 5500000")
  print("thank you for visiting my showroom")
if user_choice == 2:
 print(''' welcome sir !
           which car you want to rent
        1. Honda City
        2. Toyota Corolla
        3  Mercedes-Benz E-Class
        4  AUDI
        5. SUV''')
 rent_choice = int(input("enter your car choice"))
if rent_choice == 1:
  print("your car is rented")
  print("your car is Honda City")
  print("your car rent cost is 20000 per day")
  print("thank you for visiting my showroom")
if rent_choice == 2:
  print("your car is rented")
  print("your car is Toyota Corolla")
  print("your car rent cost is 15000 per day")
  print("thank you for visiting my showroom")
if rent_choice == 3:
  print("your car is rented")
  print("your car is Mercedes-Benz E-Class")
  print("your car rent cost is 35000 per day")
  print("thank you for visiting my showroom")
if rent_choice == 4:
  print("your car is rented")
  print("your car is AUDI")
  print("your car rent cost is 40000 per day")
  print("thank you for visiting my showroom")
if rent_choice == 5:
  print("your car is rented")
  print("your car is SUV")
  print("your car rent cost is 30000 per day")
  print("thank you for visiting my showroom")

#if user_choice == 3:
 #print("thank you for visiting my showroom")

#if user_choice == 4:
 #print("thank you for visiting my showroom")
else :
 print("thanks again !")














