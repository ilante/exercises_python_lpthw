from sys import argv # uses argv to get a filename
script, filename = argv
txt = open(filename) #opens file
print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
fileagain = input("> ")
txtagain = open(fileagain)

print(txtagain.read())


# What we want to do is "open" that file in 
# our script and print it out. However, we 
# do not want to just "hard code" the name 
# ex15_sample.txt into our script. "Hard 
# coding" means putting some bit of 
# information that should come from the user 
# as a string directly in our source code. 
# That's bad because we want it to load other 
# files later. The solution is to use argv or 
# input to ask the user what file to open 
# instead of "hard coding" the file's name.
