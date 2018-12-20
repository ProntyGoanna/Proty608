'''
Created on 19 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

#===============================================================================
# Composition of Data Structures
#===============================================================================

students = [
("John", ["CompSci", "Physics"]),
("Vusi", ["Maths", "CompSci", "Stats"]),
("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

def search_student_by_subject(subject):
    cs_students = []
    number_cs_student = 0
    for name, subjects in students :
        if subject in subjects:
            number_cs_student += 1
            cs_students.append(name)
    return (number_cs_student, cs_students)

(total_number, names) = search_student_by_subject("CompSci")
print("total number of cs students: ", total_number)
print("names of cs students: ", names)


def count_movies(tuples):
    return len(julia_more_info[-1])

julia_more_info = ( ("Julia", "Roberts"), (8, "October", 1967), "Actress", ("Atlanta", "Georgia"),
                    [ ("Duplicity", 2009),
                     ("Notting Hill", 1999),
                     ("Pretty Woman", 1990),
                     ("Erin Brockovich", 2000),
                     ("Eat Pray Love", 2010),
                     ("Mona Lisa Smile", 2003),
                     ("Oceans Twelve", 2004) ]
                   )

print("number of movies = ", count_movies(julia_more_info))    