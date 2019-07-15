#5.1

rad = 0 
deg = 1
mit = 60
sec = 60
pi  = 22/7


sec  = sec  *pi/   (3600*180) 
mit  = mit  *pi/   (60     *180)
deg = deg *        (pi       /180)
rad  = rad + deg  + mit + sec

print("The convertion in radian is : ", rad )


