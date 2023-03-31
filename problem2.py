def take_Input():
    Number1 = int(input("Enter the first value: "))
    Number2 = int(input("Enter the second value: "))
#for addition
    operator= input("enter the operand) (+):") 
     return first value,second value,operator
def declareResult():
  first value, second value, operator = getinput()
  if operand =="+":
    result= first value + second value
    print("{first value} + {second value} = {output}")
    #for subtraction
    operator= input("enter the operand) (-):") 
   return first value,second value,operator
def declareResult():
  first value, second value, operator = getinput()
  if operand =="-":
    result= first value - second value
    print(f"{first value} - {second value} = {output}")
    #multiplication
    operator= input("enter the operand) (*):") 
   return first value,second value,operator
def declareResult():
  first value, second value, operator = getinput()
  if operand =="*":
    result= first value * second value
    print(f"{first value} *{second value} = {output}")
    #for division
    operator= input("enter the operand) (/):") 
   return first value,second value,operator
def declareResult():
  first value, second value, operator = getinput()
  if operand =="/":
    result= first value / second value
    print(f"{first value} / {second value} = {output}")
  else:
    print("operator is invalid")
    displayResult()
