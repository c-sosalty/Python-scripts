t1   = [1 ,2 ,3 ,14 ,5 ,7 ,14.5 ,11 ]
i, m = 0 , 0
while i < len(t1):
      if m < t1[i]:
            m = t1[i]
      i+=1
print(m)
