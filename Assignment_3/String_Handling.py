#a,b,c=input("Enter Malformed Time String: ").split(":")
def func(a,b,c):
    
    if int(c)>59:
        sec=int(c)//60
        c=int(c)%60
        if int(b)>59:
            mins=int(b)//60
            b=int(b)%60
            b+=sec
        else:
            b=int(b)
            b+=sec
        if int(a)>12:
            a=int(a)%12
            a+=mins
        else:
            a=int(a)
            a+=mins
    elif int(b)>59:
        mins=int(b)//60
        b=int(b)%60
        if int(a)>12:
            a=int(a)%12
            a+=mins
        else:
            a=int(a)
            a+=mins
    elif int(a)>12:
        a=int(a)%12    
    return (a,b,c)


x=[1,3,5,7,8,10,12]
z=[4,6,9,11]
def func(a,b,c):
    if int(a)>31 and int(b) in x:
        mon=int(a)//31
        a=int(a)%31
        if int(b)>12:
            year=int(b)//12
            b=int(b)%12
            b+=mon
        else:
            b=int(b)+mon
    elif int(a)>30 and int(b) in z:
        mon=int(a)//30
        a=int(a)%30
        if int(b)>12:
            year=int(b)//12
            b=int(b)%12
            b+=mon
        else:
            b=int(b)+mon
    elif int(b)==2:
        if int(b)%4==0:
            if int(b)%100==0:
                if int(b)%400==0:
                    Cond=True
                else:
                    Cond=False
            else:
                Cond=True
        else:
            Cond=False
        if Cond==True:
            mon=int(a)//29
            a=int(a)%29
            if int(b)>12:
                year=int(b)//12
                b=int(b)%12
                b+=mon
            else:
                b=int(b)+mon
        else:
            mon=int(a)//28
            a=int(a)%28
            if int(b)>12:
                year=int(b)//12
                b=int(b)%12
                b+=mon
            else:
                b=int(b)+mon
    return (a,b,c)

import ipaddress
def ipaddress_2(x):
    try:
        x=int(x)
        z=ipaddress.ip_address(x)
    except:
        addr1 = ipaddress.ip_address(x)  
        return(int(addr1))

def isogram(x):
    print(True if len(list(x))==len(set(x)) else False)

x=list('ankt')
def mexican(temp):
    temp=[print("".join(x[:i])+"".join(x[i].upper())+"".join(x[i+1:])) for i in range(len(x))]

def Deleting_singal_digit(x):
    z=0
    lis_t=[]
    lis_t_2=[]
    for i in range(len(x)):
        lis_t_2=x.copy()
        lis_t_2.pop(z)
        lis_t.append(int("".join(lis_t_2)))
        z+=1
    print(max(lis_t))

from itertools import permutations
def pert(x):
    t=permutations(x)
    lis_t=[]
    for i in t:
        lis_t.append(int("".join(i)))
    print(max(lis_t))


def Highest_num_suffule(x):
    dic_t={}
    for i in x:
        if i not in dic_t.keys():
            dic_t[i]=x.count(i)
        else:
            continue
    print(dic_t)

def accumulated_strings(x):
    for i in x:
        print(i.upper()+i*x.index(i))

def rgb_hex(x):
    print(x)
    if 'x' in x[0]:
        print(x[0][:4])
        print(int(x[0][:4],16),int(x[0][4:6],16),int(x[0][6:],16))
    else:
        a,b,c=x
        print(hex(int(a))+hex(int(b)).replace("x","")+hex(int(c)).replace("0x",""))



