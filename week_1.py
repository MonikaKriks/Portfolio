#!/usr/bin/env python3
print('#task 1')
if __name__ == '__main__':
    print('Hello, World\n')

###############################################



print('#task 2')
print( 'Hello, Monika\n')

################################################

print('#task 3')
print('Temperatures that were reached over the summer:' )
temp_c= 38.4
temp_c_round= round(38.4)
temp_f =  1.8 * temp_c + 32
temp_f_round= round(1.8 * temp_c+32)
print("Temperature in Celsius: ",temp_c_round,chr(176),'C')
print("Temperature in Fahrenheit:" ,temp_f_round, chr(176),'F')

#############################################


print('\n#task 4')

matches = 609
batted = 1014
not_out = 162
scored_runs = 48426

batting_average = 1014/609
batting_ave_rounded= round(1014/609,1)
print("Geoffrey Boycott's batting average is:",  batting_ave_rounded , "hits per game.\n")

#######################################################################################

import math

print ("# task 5")
groups_needed= (113 + 175 + 12) /24
print('Total student lab groups needed:', groups_needed,'\n')
full_groups= int(groups_needed)
left_over= math.ceil(0.5)
print('Which means there will be: ')
print(full_groups,'-', 'full groups')
print(left_over,'-', 'left over group')









