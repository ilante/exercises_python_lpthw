#13 Input method to pass a viariable to a scirpt
# script is another name for a .py file.

# python3.6 ex13.py ---> ex13.py  is the argument.

from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv #argv is a list
#first argument is allways the name of the script you are running
# take wathever is in argv, unpack it and assign it to all of these variables on the left in order
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second vaiable is:", second)
print("Your third variable is:", third)
# so if cd ./Desktop the name is the argument
x = input("Give me another value")
print(x)

y=input("How long does it take you to brush your teeth?")
print(y)