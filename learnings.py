print("Hello world")
a="sukesh codes"
print(a)
print(len(a))
print(a.isalpha())
print(a.isalnum())
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.title())
print(a.count('e'))
print(a.find("o"))
print(a.find("es"))
print(a.isupper())
print(a.islower())
print(a.replace(" ","-"))
print(a.endswith("s"))
print(type(a))
b="sukesh\nsubash"
print(b)
print(b.splitlines())
print(b.splitlines(True))
c="       sukesh      "
print(len(c))
print(len(c.strip()))
print(len(c.lstrip()))
print(len(c.rstrip()))
d="3-6-2023"
print(d.partition("-"))
# string manipulation
e="sample"
print(e[1:5])
print(e[1:])
print(e[2:3])
print(e[-1])
print(e[::-1])
# arithmetic opertors
a=500
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(2**4)
# assignment operator
a=100
b=200
print(a==b)
a +=5
print(a)
a -=5
print(a)
a *=5
print(a)
a /=5
print(a)
a %=10
print(a)
# comparision or relational operator
a=10
b=20
print(a==b)
print(a!=b)
print(a==b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
# logical operator
# and
# or
# not + and
a=10
print(a>=10 and a<=20)
a=25
print(a>=10 and a<=20)

print(a>=10 or a<=25)
print( not (a>=10 and a<=20 ))
# bitwise operator
a=10
b=11
print(a&b)
print(a|b)
print(a^b)
print(~b)
print (a>>2)
print(a<<2)

# if statement and if else
a=int(input("enter number:"))
if a % 2 ==0:
    print("even")
else:
    print("odd")
    # if else
    name=input("enter name:")
age=int(input("enter age:"))

if age>=18:
    print(name, "is elible for vote")
else:
    print(name, "is not eligible for vote")
#  elif
days=int(input("enter the days :"))
if (days == 0):
    print ("good no fine")
elif(days>=1 and days<=5):
    print ("fine amount :" ,days * 0.5)
elif (days >=6 and days <=10):
    print("fine amount :" ,days*1)
elif (days >=11 and days<=15):
    print ("fine amount :",days*5)
elif (days >=16 and days<=25):
    print ("fine amount :",days*10)
elif (days >=26 and days<=30):
    print ("cancel pass")

    # nested if

    m1=int(input("enter mark1:"))
m2=int(input("enter mark2:"))
m3=int(input("enter mark3:"))
total=m1+m2+m3
average=total/3.0

print("total :" ,total)
print("average :",average)

if (m1>=35 and m2>=35 and m3>=35):
    print("pass")
    if(average>=90 and average<=100):
        print("grade : A ")
    elif(average>=80 and average<=89):
        print("grade : b ")
    elif(average>=70 and average<=79):
        print("grade : c ")
    elif(average>=60 and average<=50):
        print("grade :  ")
    
    
else:
    print("result=fail")
    print("grade : no grade")

    # while

    i=1
while(i<=10):
    print(i)
    i +=1

    print("even numbers")
    n=20
    i=2
    while(i<=20):
        print(i)
        i +=2
        
print("odd numbers")
n=20
i=1
while(i<=20):
        if(i%2==0):
            i = i+1
            continue
        print(i)
        i +=2
# break
i=1
while(i<=10):
    if(i==8):
        break
    print(i)
    i+=1
        # range
a=list(range(5))
print(a)
print(list(range(2,5)))
print(list(range(0,20,2)))
print(list(range(1,20,2)))

# for loop     using range 
for i in range(0,21,2):
    print(i)
print(list(range(1,20,)))

for i in range(5):
    a=int(input("enter number :"))
    b=int(input("enter number :"))
    print (a+b)

# sTAR pattern  in for looop
for i in range (7):
    for j in range (i):
        print ("*",end=" ")
    print("")

print (".....................................................")


for i in range(7,0,-1):
    for j in range (i):
       print ("*",end=" ")
    print("")

# abcd printing

for i in range(65,70,1):
    for j in range (65,70,1):
        print(chr(j),end="")
    print("")

    # while else i=1
while i<=5:
    print (i)
    i +=1
else:
    print("completed")
    
    #  for else

for i in range (1,21):
    print(i)
else:
    print("loop completed")
    
    # if it breaks else cant work
for i in range (1,21):
    if(i==5):
        break
    print(i)
else:
    print("loop completed")
    

    # list and tuples
    a=[1,2,3,4,55,66,77,88]
print(a)
print(type(a))
print(a[1])
print(len(a))
print(a[-1])
print(a[2:7])
print(a[:-1])
print(a[:6])


b=["a",20,[1,2,3,4],10,"sukesh",True,2.5]
print(b)
print(type(b))
print(len(b))
print(type(b[0]))
print(type(b[2]))
print(type(b[-1]))
print(type(b[-2]))
print(b[2][2])

c=[10,11,12,14,15,16]
print(c)
c.clear()
print(c)
c=[10,11,12,14,15,16,15,15,15]
d=c.copy()
print(d)

print(d.count(15))
print(d.index(15))
print(max(d))
print(min(d))

d=[10,11,12,14,15,16,15,15,15]
d.pop(0)
print(d)
d.remove(15)
print(d)
d.append(10)
print(d)

print("----------------------------")

names=["sukesh"]
print(names)
names.append("suk")
names.append("suke")
print(names)
name2=["saara","anitha"]
names.extend(name2)
print(names)

names.insert(0,"aakash")
print(names)
print("----------------------------")

print(list(range(5)))
print(list("sukesh"))
a=[15,16,17,20,37,77,88,24,33,65]
print(a)
a.sort()
print(a)
b=["sukesh","black","car","doll"]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.sort(key=len)
print(b)

print(list(range(5)))
print(list("sukesh"))
a=[15,16,17,20,37,77,88,24,33,65]
print(a)
a.sort()
print(a)
b=["sukesh","black","car","doll"]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
b.sort(key=len)
print(b)
# tuples
# immutable
a=("a","b",21,"sukesh",True,35.5)
print(a)
print(type(a))
print(a[1])
print(a[0:1])
print(len(a))
print (type(a[0]))
print(a)
b=list(a)
print(b)
b.append("subash")
print(b)
b.insert(22,33)
print(b)
a=tuple(b)
print(a)
for i in a:
    print(i)
if "sukesh" in a:
    print("yes")
else:
    print("no")
a=(1,2,3,4,5,6,7,8)
b=(9,10,11,12,13,14,15,16,17)
c=a+b
print(c)
print(len(c))
print(c.count(1))
c=(a,b)
print(c)
print(min(a))
print(max(a))

x=("sukesh",)*5
print(x)

# set
a={1,2,3,4,5}
b={5,6,7,8,9,10}
name={"sukesh","subash","suk","sam","selva"}
print(name)
print(type(name))
for i in name:
    print(i)
name.add("sara")
print(name)
name.update(a)
print(name)
name.remove(1)
print(name)
name.discard(1)
print(name)
name.pop()
print(name)
name.clear()
print(name)
del name
print(name)
name={"sukesh","subash","suk","sam","selva","sukesh"}
print(name)
print(len(name))
# with numbers
a={1,2,3,4,5}
b={5,6,7,8,9,10}
c={'a','b','c'}
d=a.union(b)
print(d)
e=a.union(c)
print(e)

a.update(b)
print(a)
a={1,2,3,4,5}
b={5,6,7,8,9,10}

c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
a={1,2,3,4,5}
b={5,6,7,8,9,10}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

a={5,6,7,8,9,10}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)

c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)


# dictionary
a={
    "name":"sukesh",
    "age": 22,
    "isstudying":True,
}
print(a)
print(type(a))
print(a["name"])
print(a["age"])
print(a.get("isstudying"))

print(a.keys())
print(a.values())
print(a.items())
for i in a:
    print(i,"",a[i])
    
for i in a.values():
    print(i)

for i in a.keys():
    print(i)
for x,y in a.items():
    print(x,y)
    
if "age" in a:
    print("yes")

if "gender" in a:
    print("gender")

a.update({"gender":"male"})
print(a)
a["age"]=32
print(a)

a.pop("age")
print(a)
a.clear()
print(a)
del a
print(a)
user={
    "a": {
    "name":"sukesh",
    "age": 22,
    "isstudying":True,
}
 "b": {
    "name":"subash",
    "age": 25,
    "isstudying":false,
}
}
print(user)


# is is not 
a=[1,2]
b=[1,2]
c=[1,2]
d=a
print(a is d)
print( a is not d)
print(a == d)
print (a != d)

print ( a is b)
print(a is not b)
print (a == b)
print(a!=b)
print ( a is c)

# member function list tuple are in atha or not

a=[10,33,55,66,77,88,45]
print(45 in a)
print(22 in a)
print (22 not in a)

# functions
def welcome():
    print("welcome to tutor joes")

welcome()
welcome()
welcome()
welcome()

#  9types
# No Return Type Without Argument Function in Python
def add():
    a=int(input("enter a: "))
    b=int(input("wnter b: "))
    c=a+b
    print("total : ",c)

add()

# No Return Type With Argument Function in Python
def sub(a,b):
    
    c=a-b
    print("total : ",c)

sub(222,111)
# Return Type Without Argument Function in Python
def mul():
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    c=a*b
    return c

print("total :",mul())

x=mul()
print("total",x)


# Return Type With Argument Function in Python

def div(a,b):
    c=a/b
    return c

x=div(10,5)
print("value",x)


# Arbitrary Arguments Function in Python

def user(*students):
    print(students)
    for i in students:
        print(i)
user("ram","sam")
# Keyword Arguments Function in Python

def student(name,age):
    print(name,"age is ",age)

student(age=22,name="sukesh")
# Arbitrary Keyword Arguments in Python
def biodata(**data):
    print(data)

biodata(name="sukesh",age=22,gender="male")

