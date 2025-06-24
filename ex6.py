
#****************************************************************************#
# here we use Format characters within strings, it stores information within #
# the variable, and sends it to where it is refered to                       #
# ***************************************************************************# 

#declaring a variable named num with the value 10
num = 10
#using a formated variable 
x = f"There are {num} types of people."
#storing string data into the "binary" and "do_not" variables
binary = "binary"
do_not = "don't"
#using formated variables once more
y = f"those you know {binary} and those who {do_not}"

#printing our variables out, that contain our strings
print(x)
print(y)

#printing out strings with formated variables within the print statment
print(f"i said: {x}")
print(f"i also said: {y}")

#storing a boolean value in a variable
hilarious = False
joke_evaluation = f"Isn't that joke so funny?! {hilarious}"
#printing out the Boolean variable, within the string
print(joke_evaluation)


w = "This is the left side of..."
e = "a string with a right side."
#concatenating two strings
print(w+e)