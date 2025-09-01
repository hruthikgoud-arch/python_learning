'''def info(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(f"the sum of a and b:{c}")
    print(f"the sub of a and b:{d}")
    print(f"the multiple of a and b:{e}")
info(3,5)    
def personal(name,age):
    print(f"my name is:{name}")
    print(f"my age is:{age}")
a= input("name:")
b= input("age:")
personal(a,b)
def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    if b!=0:
        return a/b
    else:return"division by zero not allowed"
x=int(input("enter your name"))
y=int(input("enter your age"))
print("addition:",add(x,y))
print("division:",add(x,y))
def sumop():
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    c=a+b
    e=a*b
    if b==0:
        print("division by zero not possible")
    else:
        f=a/b
        print("div of ({},{}is={}".format(a,b,f))
    print("sum of ({},{})is={}".format(a,b,c))
    print("mul of ({},{}is={}".format(a,b,e))
sumop()'''
def sumof():
    a=float(input("enter first value:"))
    b=float(input("enter second value:"))
    c=a+b
    e=a*b
    if b==0:
        print("division by zero not possible")
    else:
         f=a/b
    result=("sum {}and{}={}\nmul {}and{}={}\ndiv {}and{}={}\n").format(a,b,c,a,b,f,a,b,e)
    return result
print(sumof())
