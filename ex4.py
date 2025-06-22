
#*****************************************************#
# using variables in print methods, storing different #
#*****************************************************#

#number of total cars
cars = 100
#number of seats in a car
space_in_car = 4.0
#total number of drivers
drivers = 30
#total number of passengers
passengers = 90
#total number of cars that have no drivers hence are not driven
cars_not_driven = cars - drivers
#cars that are driven
cars_driven = drivers
#the number of people can use the space in the car
carpool_capacity = cars_driven * space_in_car
#average number of people that can fit in a car
average_passangers_per_car = passengers / cars_driven


print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today")
print("We need to put about", average_passangers_per_car, "in each car")
