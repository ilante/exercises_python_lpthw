#What strings do: 
# string usually is a bit of text to be displayed to
# someone or to "export" out of the program you are wirting.
types_of_people = 10
x = f"There are {types_of_people} types of people."
#assigned var x to the fstring

binary = "binary" #assigned binary to the var binary
do_not = "don't" #assigned 'dont' to var do_not
y = f"Those who know {binary} and those who {do_not}."
#assigned another fsting to var y
print(x) #prints output to the screen of x and y
print(y)

print(f"I said: {x}") #I can use it to change the meaning of a repeating sentence
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#so why is the {} empty? Why does it insert the boolean

print(joke_evaluation.format(hilarious)) #calles the fstring with the variable joke_evaluation
w = "This is the left side of..."
e = "a string with a right side."

print(w+e)

