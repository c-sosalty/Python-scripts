from math import *
a ,b ,c = input("Inserer la longuer des 3 cotés > A:" ),input("B :") , input("C :")
a ,b ,c = int(a) , int(b) , int(c)
Air     =0
periM   =a+b+c
DPeriM  =periM/2
Air  = sqrt(DPeriM*(DPeriM-a)*(DPeriM-b)*(DPeriM-c))

print("Le perimetre =",periM ,"m")
print("L'air = " ,       Air ,"m²")

