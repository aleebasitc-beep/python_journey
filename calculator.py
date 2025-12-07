print('---Welcome to the calculator---')
while True:
 num1 = int(input('enter number: '))
 num2 = int(input('enter number: '))
 print("Operator: (+, -, /, *) or 'q' to quit: ")
 op = input('choose an Operator: ')
 if op == "+":
  print("Result: ", num1 + num2)
 elif op == "-":
  print("Result: ", num1 - num2)
 elif op == "*":
  print("Result: ", num1 * num2)
 elif op == "/":
  if num2 == 0:
   print('Error: zero cannot be divided')
  else: 
   print("Result: ", num1 / num2) 
 elif op == "q":
  print("Exiting calculator...\nThankyou for using!")
  break
 else:
   print("invalid try again!")  