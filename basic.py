# Building basic math program that adds sub mult def mudule power.gi
while True:
 print("1. for addition +")
 print("2.for subtract -")
 print("3.for multiplication *")
 print("4.for devision /")
 print("5.for madule or reminder %")
 print("6.for index or power **")
 selec=input(" select an operator: ")
 if selec=="+":
   num1=int(input("Enter for number 1: ")) 
   num2=int(input("Enter for number 2: "))
   result=num1+num2
   print(f'your addition is {result}')
 elif selec=="-":
   num1=int(input("Enter for number 1: "))
   num2=int(input("Enter for number 2: "))
   result=num1-num2
   print(f'your subtraction is {result}')
 elif selec=="*":
   num1=int(input("Enter for number 1: "))
   num2=int(input("Enter for number 2: "))
   result=num1*num2
   print(f'your multipication is {result}') 
 elif selec=="//":
   num1=int(input("Enter for number 1: "))
   num2=int(input("Enter for number 2: "))
   result=num1//num2
   print(f'your defision is is {result}') 
   if num1==0:
     print("zero is not devisible")
 elif selec=="%":
   num1=int(input("Enter for number 1: "))
   num2=int(input("Enter for number 2: "))
   result=num1%num2
   print(f' {num1,num2} the reminder is {result}') 
 elif selec=="**":
   num1=int(input("Enter for number 1: "))
   num2=int(input("Enter for number 2: "))
   result=num1**num2
   print(f'{num1,'power',num2} is  {result}') 
   
 else:
  print("invalid operator")
   
 kont=input("press Y to countinue or N to finish:  ").capitalize()
 if kont!="Y":
   print("out of program bye")
   break





