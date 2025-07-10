the_count = [1,2,3,4,5]
fruits = ['apples','orange','pears','aprocots']
change = [1,'pennies',2,'dimes',3,'quarters']

# This first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")

# also we can go through mixed lists too
# notice we have to use %r since we dont know whats in it

for i in change:
    print(f"i got {i}")

#we can also build list, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #append is a function that list understand
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")