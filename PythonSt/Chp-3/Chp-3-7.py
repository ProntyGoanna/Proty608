'''
Created on 17 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

students = [
("John", ["CompSci", "Physics"]),
("Vusi", ["Maths", "CompSci", "Stats"]),
("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

counter = 0
for name, subject in students:
    print(name, "takes", len(subject), "courses")    
    if "CompSci" in subject:
        counter += 1      
print("The number of students take CompSci is ", counter)