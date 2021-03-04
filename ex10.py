# see Escape sequences 65
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \ a \ cat."
print("one \ slash") # it should not work but it does

print("two \ cat \ slash")
print("one error \ ") # prints the slash as well - 
# so the point is if thers no spc
#so one \ gets printed as well
print("slash\middle")
x='\a'
for e in range(4):
    print(x)
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("""
Hi Giacomo.
We should eat one "pannini"
The zucchini are so good today.
""")