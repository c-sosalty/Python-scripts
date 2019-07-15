#5.2

rad = 0.5 
deg = 0
mit = 0
sec = 0

pi = 22/7 

sec = rad * (60*60*180) /pi 
mit = rad *    (60*180) /pi
deg = rad *        180  /pi

mit = mit % 60
sec = sec % 60

print(rad , "radian(s) is = to  " ,deg  ,'°'  ,mit ,"'" ,sec ,"''"  )

