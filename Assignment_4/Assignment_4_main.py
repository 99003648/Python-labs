from Assignment_4 import *

mb = mobile_billing(30,100,'POSTPAID',50,30)
print(mb.totalbill())

Ax = Quad_point(10,-2)
print(Ax.axis())

cr = circle(2.5)
print("Areat of Circle:-", cr.area())
print("Circumference of circle:-",cr.circumference())

tr = triangle(10,10,10)
print("Circurmfrence of triangle:-",tr.circumference())
print("Area of triangle:-",tr.area())

re = rectangle(10,8)
print("Area of rectangle:-",re.area())
print("Circurfance of rectangle:-",re.circumference())


b1 = box(10,5,3)
print(b1.volume())
print(b1.display())

ob = color((255,255,255))
print(ob.form_color())
