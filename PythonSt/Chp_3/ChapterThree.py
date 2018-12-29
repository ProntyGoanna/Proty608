'''
Created on 14 Dec. 2018

@author: E491529
'''

if __name__ == '__main__':
    pass

def print_lyrics():
    print("I'm a lumberjack, and I am okay.")
    print("I sleep all night and I work all day")
    
print_lyrics()    

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()



def right_justify(aString):
    print(' ' * (70-len(aString)) + aString)
    
right_justify('Two Steps from Hell:')
right_justify('Victory')

def do_twice(f, arg):
    f(arg)
    f(arg)
    
def do_twiceWithoutArg(f):
    f()
    f()

do_twice(right_justify,'Lumberjack, I am ok!')    
do_twiceWithoutArg(repeat_lyrics)


def print_frame1():
    print('+','-'*4,"+",'-'*4,'+')
    
def print_frame2():
    print('|',' '*4,'|',' '*4,'|')
    
print_frame1()
do_twiceWithoutArg(print_frame2)
do_twiceWithoutArg(print_frame2)
print_frame1()
do_twiceWithoutArg(print_frame2)
do_twiceWithoutArg(print_frame2)
print_frame1()    