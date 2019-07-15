#Algorithme pour convertir a partir de seconde en minut , heure , jours etc...

s , m , h , j , a  = 31536000 , 0 , 0 ,0 ,0 

m = s // 60
h = m // 60
j = h // 24
a = j // 365

s = s % 60
m = m % 60
h = h % 24
j = j % 365

print( a , ":", j ,":",  h ,":",  m ,":", s )

