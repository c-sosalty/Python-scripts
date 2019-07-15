ph = 'hallo worle'
cn = 'a'
c  = ''
a  =  0
while a < len(ph):
      c = ph[a]
      if c == cn:
            print( '[',cn,']','in the idex number :', a )
            break
      a+=1
      if a == len(ph):
            print('no ', cn )

