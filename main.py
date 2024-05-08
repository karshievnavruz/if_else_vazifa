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
#12 Numbers  A , B and C are given. Determine the sum of the two largest numbers from them.

"""
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))

if a>c and b>c:
    print(a+b)
elif b>a and c>b:

    print(b+c)
elif c>b and a>b:
    print(c+a)
else:
    print("error")
"""
#13 Nummber A  is given. Determine if A is a prime number.

"""
a = int(input("Iltimos, son kiriting: "))

num = a
if num <= 1:
    print(num, "tub emas.")
elif num <= 3:
    print(num, "tub son.")
elif num % 2 == 0 or num % 3 == 0:
    print(num, "tub emas.")
else:
    i = 5
    while i * i <= num:
        print(i,num)
        if num % i == 0 or num % (i + 2) == 0:
            print(num, "tub emas.")
            break
        i += 6
    else:
        print(num, "tub son.")"""
"""
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Sonni o'qib olish
a = int(input("Iltimos, son kiriting: "))

# Berilgan sonning tub son ekanligini tekshirish
if is_prime(a):
    print(a, "tub son.")
else:
    print(a, "tub emas.")

"""

#14 Numbers A and B are given.  A and B, i.e. both are prime numbers define

"""
a=int(input("A="))
b=int(input("B="))

if a%2==1 and b%2==1:
    print(True)
else:
    print(False)
"""

#15  Numbers A and B are given. Determine whether A or B is a large number.
"""
a=int(input("A="))
b=int(input("B="))

if a%2==1 or b%2==1:
    print(True)
else:
    print(False)"""

#16 Numbers A , B and C are given.Determine whether A, B, and C are positive. 

a=int(input("A="))
b=int(input("B="))
c=int(input("C="))

if a%2==1 or b%2==1:
    print(True)
else:
    print(False)