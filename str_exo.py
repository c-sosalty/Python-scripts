#5.9  -put the string to the inverse
#5.10 -see if it's a palindrome

ph   = "bob"
ph_x = ""
ph_l = len(ph)
n    = 0

while  n < ph_l:
      n+=1
      ph_x += ph[ph_l - n]
if ph == ph_x:
      print("It's a palindrome")
print(ph_x)
