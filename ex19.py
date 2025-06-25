
#******************************************************************************#
# Here we have functions that take in arguments, and we use the arguments as   #
# formatte variables, we also pass in variables as arguments into the function #
# when we call it, we are also doing math inside of put function               #
#******************************************************************************#


def cheese_and_cracker(cheese_count,boxes_of_crackers):
    print(f"i have {cheese_count} many cheesesss!!!")
    print(f"You have {boxes_of_crackers} many boxes of crackers")
    print("man thats enough to save starving african children")
    print("get a blanket\n")

print("we can just give the function numbers directly")
cheese_and_cracker(20,20)

print("Or, we can use variables in our script")

boxes_of_crackers = 20
cheese_count = 20

cheese_and_cracker(cheese_count,boxes_of_crackers)

print("We can even do math inside too:")
cheese_and_cracker(10 + 2,50/2)

print("And we can combine the two, variables and math")

cheese_and_cracker(cheese_count + 1000, boxes_of_crackers + 150)