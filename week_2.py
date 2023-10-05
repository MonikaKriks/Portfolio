print("#task 1")
name= input("Hello, what is your name? ")
print("Hello",name,",","Good to meet you!\n" )

##############################################

print("#task 2")
temp_c =int(input("Enter a temperature in Celsius: "))
temp_f= (temp_c * 1.8) + 32
print(temp_c,chr(176),"C", "is equivalent to", temp_f, chr(176),"F\n")

###############################################

print("#task 3")
total_students= int(input("How many students? "))
students_per_group= int(input("Required group size? "))
groups= total_students / students_per_group
left_over= total_students % students_per_group
print(" There will be", groups, "groups with", left_over, "students left over")

#################################################

import math as m
print("#task 4")
sweets_count= int(input("How many sweets do you have? "))
children_there= int(input("How many children are in the class today? "))
sweets_for_each= (m.floor(sweets_count /children_there))
remaining_sweets=(sweets_count % children_there)
print("Give",sweets_for_each,"sweets to each pupil.")
print("Sweets remaining in a tub: ",remaining_sweets)
