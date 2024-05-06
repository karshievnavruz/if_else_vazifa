#1 A nummber is given. Detemine whether it is  positive or negative.

"""
a=int(input("A="))
if a>0:
    print(f"The nummber {a} is positive")
elif a<0:
    print(f"The nummber {a} is negative")
else:
    print("The nummber is zero")
"""
#2 A nummber is given. Detemine whether it is even or odd
"""
a=int(input("A="))
if a%2==0:
    print(f"The nummber {a} is even ")
else:
    print(f"The nummber {a} is odd")
"""
#3  nummber A is given (1-7). Detemine whate day of the week this  number is.
"""
a=int(input('A='))

if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wendnesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print(f"{a} is not  a number between (1-7)")
"""
#4 A nummber is given. if A is positive, add 2 to it , if it is negative , subtract 2 from it 
"""
a=int(input("A="))
if a>0:
   print(a+2)
elif a<0:
   print(a-2)   
else:
   print("zero")
"""
#5 Numbers A and B  are given. Does this satisfi our condition A>3 and B<=6? check if you like.
"""
a=int(input("A="))
b=int(input("B="))
if a>3 and b<=6:
    print(True)
else:
    print(False)
"""

#6 Numbers A and B are given. Does this satisfi our condition A<2 and B>=-2  check if you like.
"""
a=int(input("A="))
b=int(input("B="))

if a<2 and b>=-2:
    print(True)
else:
    print(False)
"""
#7 Numbers A and B are given. Print the first large one, then the small one.
"""
a=int(input("A="))
b=int(input("B="))
if a>b:
    print(f"{a} , {b}")
else:
    print(f"{b} , {a}")
"""
#8 Numbers A and B are given(of float type).Which one of them has a small remainder? if so, determine this number.
""" 
a=float(input("A="))
b=float(input("B="))
a1=a%1
b1=b%1
if a1>b1:
    print(b)
if b1>a1:
    print(a)
else:
    print("=")
"""
#9 Numbers A, B and C are given. Whether A < B < C meets our condition define.
"""
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))

if a<b and b<c:
    print(True)
else:
    print(False)
"""
#10 Numbers A, B and C are given . Determine whether the number of B is between A and C.
"""
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))

if a<b and b<c:
    print(True)
elif c<b and b<a:
    print(True)
else:
    print(False)
"""

#11 Numbers A ,B and C are given.  Find out how many of them are positive.

"""
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
n=0
if a>0:
    n+=1
if b>0:
    n+=1
if c>0:
    n+=1
print(n)
"""

