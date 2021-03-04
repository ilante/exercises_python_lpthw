name = 'Ila A. Engl'
age = 30 #unfortunately not a lie
height = 154 #inches
cmheight = round(height/28.3496)
weight = 45 #lbs
kgweight = round(weight/0.453592)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"She's {cmheight} inches tall.")
print(f"She's {kgweight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depepnding on the coffee.")


total = age + height + weight
print(f"If I add {age}, {round(cmheight)}, and {round(kgweight)} I get {total}.")

#ex5

# "format string." Every time you put 
# " (double-quotes) around a piece of text 
# you have been making a string. A string is
# how you make something that your program 
# might give to a human. You print strings, 
# save strings to files, send strings to web 
# servers, and many other things.
# Strings are really handy, so in this 
# exercise you will learn how to make strings 

# that have variables embedded in them. You 

# embed variables inside a string by using a 

# special {} sequence 
# 
# and then put the variable
#  you want inside the {} characters. You also 
# must start the string with the letter f for 
# "format", as in f"Hello {somevar}". This 
# little f before the " (double-quote) and the 
# {} characters tell Python 3, "Hey, this string 
# needs to be formatted. Put these variables 
# in there."