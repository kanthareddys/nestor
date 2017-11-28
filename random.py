import random 
n=random.randint(1,99)
guess=int(raw_input("enter your number"))
def __init__(self,guess):
    while n!="guess":
   
        if guess<n:
            print"you enterd low number"
            guess=int(raw_input("enter your number"))
            
        elif guess>n:
             print"you ented high value"
             guess=int(raw_input("enter your number"))
       
        else:
            print"ur are correct"
            break
            print   


def retry_self():
    if guess<4:
        print"you have lived"
    else:
        print"you died"
        return
__init__(2)