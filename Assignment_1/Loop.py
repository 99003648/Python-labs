def Digital_root(x):
    while x>9:
        su_m=0
        for i in str(x):
            su_m+=int(i)
            x=su_m
    return x

def Prime_range(num1,num2):
    for num in range(num1,num2+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num

def triangual(x):
    sum=0
    for i in range(1,x+1):
        for j in range(1,i+1):
            sum+=j
    return sum

def multiple_(x):
    z=0
    lis_t=[]
    lis_t_2=[]
    for i in range(len(x)):
        lis_t_2=x.copy()
        lis_t_2.pop(z)
        lis_t.append(int("".join(lis_t_2)))
        z+=1
    return max(lis_t)


def super_prime(upper):
    lis_t=[]
    for num in range(2,upper+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            lis_t.append(num)
            for i in range(2,len(lis_t)):
                for j in range(2,i):
                    if i%j==0:
                        break
    else:
        print(lis_t[i-1])


def Combination(x,y,z):
    if z>x:
        print("You Can't Select This Much")
    else:
        n=1
        c=1
        r=1
    for i in range(1,x+1):
        n*=i
    for i in range(1,z+1):
            r*=i
    for i in range(1,x-z+1):
            c*=i
            return n/(c*r)

def pattern(n):
   
    # number of triangle
    i = 0
    j = 0
    for i in range(n):
        for j in range(i):
            print(j,end='')
       
        print("")
   

      # number of Pascal
    i = 1
    j = 1
    k = 1
    for i in range (1,n+1):
        for k in range(1,n-i+1):
            print(" ",end='')
        for j in range(1,i+1):
            print(j,end='')
        for j in range(2,i+1):
            print(j,end='')    
       
        print("") 