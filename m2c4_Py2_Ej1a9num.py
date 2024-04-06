#Ejercicio 1:
names_list = ['Lisa', 'Eric', 'Mark', 'Jordan']
print(names_list)

tags_tuple = ('Python', 'SCSS', 'REACT')
print(tags_tuple)

float_sale_price = 13.99
print(float_sale_price)

integer = 134 
print(integer)

from decimal import Decimal
product_cost = Decimal (12.54373)
qty = 66
print(product_cost * qty) 

user_dictionary = {
  'name': 'Jordan', 
  'age': 29, 
  'job': 'programmer'
  }
print(user_dictionary)

#Ejercicio 2:
float_sale_price = 13.99
print(round(float_sale_price))
import math
float_sale_price = 13.12
print(math.ceil(float_sale_price))

#Ejercicio 3:
import math
float_sale_price = 13.99
print(math.sqrt(float_sale_price))

#Ejercicio 4:
first_element = user_dictionary['name']
print(first_element)

#Ejercicio 5:
second_element = tags_tuple[1]
print(second_element)

#Ejercicio 6:
add_element = names_list.append('Michael')
print(names_list)

#Ejercicio 7:
names_list[0] = 'Raphael'
print(names_list)

#Ejercicio 8:
names_list.sort()
print(names_list)

#Ejercicio 9:
tags_tuple += ('Javascript',)
print(tags_tuple)