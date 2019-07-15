lvalue = []
value  = "none"
while value != "" :
      value = input("Input a value :")
      if value == "":
            break
      lvalue.append(int(value))
print(lvalue)
