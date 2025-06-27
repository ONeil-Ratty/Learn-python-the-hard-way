from sys import argv

#takes command line arguments and stores it in the variables
script, filename = argv

#uses the information in the commmand line to open a txt file
txt = open(filename)

#displaying the command argv using formatte variables
print("Here's your file %r" %filename)
#printing out the "opened txt file" and reading its contents
print(txt.read())

#doing it again with an input method
print("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

print(txt_again.read())