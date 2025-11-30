print('---Welcome to the calculator---')
while True:
 num1 = int(input('enter number: '))
 choose = input('choose (+, -, *, /): ')
 num2 = int(input('enter number: '))
 if choose == "+":
  print(num1 + num2)
 elif choose == "-":
  print(num1 - num2)
 elif choose == "*":
  print(num1 * num2)
 elif choose == "/":
  if num2 == 0:
   print('zero cannot be divided')
  else: 
   print(num1 / num2) 
 else:
   print("invalid try again!")  