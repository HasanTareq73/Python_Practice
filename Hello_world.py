print ("Hello world")

# this is a comment 

"""
Hello, this is Mahdi, I'm learner 

"""
if 5 > 2 :
    print("Five is greater then two")

X=5
Y= 'Mahdi'
Z= 3.1416

print(f"this is {X} ")
print (f"this is {Y}")


print(Z)

myvar = "John"
my_var = "John"

x, y, z = "Orange", "Green", "Red"

print(x)
print(y)
print(z)



fruits = ["äpple","banana","cherry"]

a,b,c=fruits

print(a)
print(b)
print(c)

# outpur variable
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


#Output variable use the + operator

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#output multiple variables, support different data types:

M = 5
N = "Mahdi"
print(M,N) 


#Global variable 

G= "awesome"

def myfunc():
    print("Python is ", X)

myfunc()

print("Golang also " , X)


#use the global keyword, the variable belongs to the global scope:
def myfunction(): 
    global G
    G = "Fantastic"
myfunction()

print ("Python is " + G)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:


G= "awesome"

def myfunction(): 
    global G
    G = "Fantastic"
myfunction()

print ("Python is " + G)



