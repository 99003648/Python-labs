'''def make(li):
    print("Enter number of elements in list:")
    list1=[li]
    print("Enter elements:")
    for i in range(l):
        list1.append(int(input(li)))
    print(list1)
    return list1'''
    
def Stray(li):
    list1=li
    for i in list1:
        for j in range(len(list1)):
            if i!=list1[j]:
                print  ("Stray number is:",list1[j])

def mean(li):
    list1=li
    sum=0
    for i in list1:
        sum=sum+i
    avg=sum/len(list1)
    print("Mean is:",avg)
    
    l=[]
    for i in list1:
        if i==avg:
            return "closest number to mean is:",i
        a=i%avg
        l.append(a)
    b=l.index(max(l))

    return "closest no. to mean :",list1[b]

def Missing(li,l2):
    #print("Enter the original list")
    l1=set(lis_t1)
    #print("Enter modified list")
    l2=set(lis_t2)
    l3=l1-l2
    print("modified list",l3)
lis_t1 =[10,20,30,40]
lis_t2 =[11,20,50,40]

def diff_2_low(li):
    l=li
    l.sort()
    print(l)
    a=l[1]-l[0]
    print(a)

def smaller_mean(li):
    list1=li
    sum=0
    for i in list1:
        sum=sum+i
    avg=sum/len(list1)
    print("Mean is:",avg)
    count=0
    for i in list1:
        if i<avg:
            count+=1
    return count
