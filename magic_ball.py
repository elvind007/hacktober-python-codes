import random
a = ["stay in class","go to pg and prepare for exam","consontrate in class that is important in exam second internal","don't think bullshit stay in class give efferet","give hard effert to steady","Try again"]

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')
print("Whats your name?: ")
name = input()
print("hello "+name)
while True:
  print("ask me any questions?: ")
  input()
  print(a[random.randint(-2,len(a)-3)])             #(0,len(a)-3)])
  print("do you want to ask any other questions?(Y/N): ")
  replay=input()
  if replay=="Y":
    print("Cool, lets play again")
  else:
    print("Good Bye!!")
    break



    #Using the same pattern of code , make a weather prediction app using Python.

  

