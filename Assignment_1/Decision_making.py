#Biggest of three/four numbers
def max_num(num1,num2,num3):
    x=max(num1,num2,num3)
    return x
def armstorng(n):
    sum=0
    r=n
    while(r>0):
        d=r%10
        sum += d**3
        r//=10
    if(n==sum):
        return "Number is Armstrong",n
    else:
        return  "Number is not armstrong",n

def reverse(num):
    rev=0
    while(num>0):
        Rem= num%10
        rev=(rev*10)+ Rem
        num=num//10
    return rev

def hcf(num1,num2):
  
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            hcf = i
            
            return hcf

def lcm(num1,num2):
    if(num1>num2):
        temp = num1
    else:
        temp= num2
    while(True):
        if((temp% num1==0) and (temp%num2==0)):
            lcm1 = temp
        break
        temp+=1
        return lcm1

def check_leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return 'Leap Year'
            else:
                return 'not leap year'
        else:
         return 'Leap Year'
    else:
        return 'not leap year'

def type_triangle(x,y,z):
    if(x**2+y**2==z**2) or (y**2+z**2==x**2) or (z**2+x**2==y**2):
        return ('Right angle')
    elif(x ==y and y==z):
        return ("equilateral triangle")
    elif((x==y and x!=z) or (y==z and y!=x) or (z==x and z!=y)):
        return ("isocelous Triangle")
    else:
        return "scalene"

def Quad_equation(a,b,c):
    dt = (b*b-4*a*c)
    if dt==0:
        return -b/(2*a),-b/(2*a)

    else:
        return -b+(dt**0.5)/(2*a),(-b-dt**0.5)/(2*a)

def quadrant(a,b):
    if(a > 0 < b ):
        return "first Qudrant "
    elif(a<0<b):
        return "Second Qudrant"
    elif( a < 0 > b ):
        return "third Qudrant"


def fact(num):
    fact=1
    if (num<0):
        return ("Factorial not exist")
    elif(num == 1):
        return ("factoriai of 1 is 0")
    else:
        for i in range(1, num+1):
            fact = fact * i
        return fact

def fabnocci(num):
    n1=0
    n2=1
    for i in range(2,num):
        n3=n2+n1
        print(n3)
        n1=n2
        n2=n3

def sum_factor(num):
    sum =0
    if(num<0):
        print("Not find Factor")
        for i in range(1,num+1):
            if(num%i==0):
                sum+=i
    return(num)

def check_volwes(ch):
    if(ch=='a' or ch=='e 'or ch=='i' or ch=='o' or ch=='u'):
         return 'volwes'
    else:
        return 'consonent'

def choice_arthimetic(a,b,c):
    if (c=='+'):
        return a+b
    elif(c=='-'):
        return a-b
    elif (c=='/'):
        return a//b
