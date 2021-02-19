#Implement Mobile billing Customer class
'''class Bank_account:
    
    def __init__ (self,Ac_no,balsnce):
        self Ac_no = Self.Ac_no
        self balance = self .balance
    def credit(self,cr):
        return total_balance+=cr
'''
    


'''class mobile_billing:
    def __init__(self, time, sms, service, carry_amt, addon):
        self.time = time # total outgoing call time
        self.sms = sms # total outgoing sms
        self.service = service # Type of service
        self.carry_amt = carry_amt # Previous unpaid balance
        self.addon = addon # Any add-on service
        self.bill = 0 # Bill amount at start of the month
        if self.service == 'POSTPAID':
            self.callrate = 0.01
            self.smsrate = 1
        else:
            self.callrate = 0.005
            self.smsrate = 0.5
    def totalbill(self):

        self.bill += self.time * self.callrate + self.sms * self.smsrate + self.carry_amt
        if self.addon:
            self.bill = self.bill + 10
            return self.bill'''

  #Implement Point as a class
'''class Quad_point:

    def __init__(self, x, y):
        self.x = x                
        self.y = y     

    def axis(self):              
        if self.x > 0:
            if self.y > 0:
                return "first Quadrent",1
            else:
                return "Second Quadrent",2
        else:
            if self.y > 0:
                return "Third Quadrent",3
            else:
                return "fourth Quadrent",4
                def __str__(self):
                    return f"({self.x}, {self.y})"  
                    
                    def dist_origin(self):       
                        return round(pow((self.x**2 + self.y**2), 0.5), 3)'''
'''class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        return 2*3.141*self.radius
    
    def area(self):
        return 3.141 * (self.radius ** 2)'''

'''class triangle:
    def __init__(self,l,b,h):
        self.l = l
        self.b = b
        self.h = h

        self.s = (self.l + self.b + self.h)/2

    def  circumference(self):
        return self.l+ self.b+ self.h
    def area(self):
        return pow(self.s*(self.s-self.l)*(self.s-self.b)*(self.s-self.h), 0.5)

class rectangle():
    def __init__ (self,len,wed):
        self.len = len
        self.wed = wed
    def area(self):
        return self.len * self.wed
    def circumference(self):
        return 2*(self.len+self.wed)'''

'''class box:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
 
    def volume(self):
        return self.length * self.breadth * self.height
 
    def display(self):
        print(f"Length = {self.length}, Breadth = {self.breadth}, Height = {self.height}")'''

'''import webcolors
class color:
    
    def __init__(self, hex_value):
        self.red = hex_value[0]
        self.green = hex_value[1]
        self.blue = hex_value[2]
        self.hex_value = hex_value
    
    def form_color(self):
        try:
            return webcolors.rgb_to_name(self.hex_value)
        except ValueError:
            print("Invalide color code")


