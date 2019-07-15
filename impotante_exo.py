l1     =[32 , 5 , 12 ,8 , 3, 75 ,2 ,15]
lp ,li =[] ,[]
i      =0
while i < len(l1):
      if l1[i] % 2 == 0:
            lp.append(l1[i])
      else:
            li.append(l1[i])
      i+=1
print("Pair list:" ,lp)
print("No pair list :", li)



lword   =["Spirituality","dinne","islam","python","charisme","muscu","prestige"]
lwp6    =[]
lwm6    =[]
n       =0
while n < len(lword):
      if  len(lword[n]) < 6:
            lwm6.append(lword[n])
      else:
            lwp6.append(lword[n])
      n+=1
print (lword)
print (lwp6 , lwm6)


























