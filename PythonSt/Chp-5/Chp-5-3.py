'''
Created on 19 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass
import math
#===============================================================================
# Tuples
#===============================================================================

#-------Tuples creation
julia = ("Julia", "Robers", 1967, "Duplicity", 2009, "Actress", "Atalnta, Georgia") 

#Access the the elements
print(julia[3:]) 


#Tuple assignments
(name, surname, year_burn, movie, year_movie, profession, birthplace) = julia # unpacking
print(name, surname, year_burn, movie, year_movie, profession, birthplace, end=(". \n")) 

#Use tuple to swap values
a = 10
b = 7
print("before swapping: a =  {0}, b = {1}".format(a, b))
print((a, b))
print((b, a))
(a, b) = (b, a)
print("after swapping: a =  {0}, b = {1}".format(a, b))


#Tuple as return value

def circle_stats(r):
    """ Return (circumference, area) of a circule of radius r """
    circumference = 2 * math.pi * r
    area = math.pi * r * r 
    return (circumference, area)

print(circle_stats(10))

