import random
import string
string.ascii_letters
list=["apple", "cherry", "doubleK", "mic", "jerry", "cat", "dog"]
print("This script is prepared by ECHOSNIPER")
print("This is a Password Generator")
print("-----------------------------------------------------")
x=0
list2=[]
while x<6:
    list2.append(random.choice(string.ascii_letters))
    x=x+1
x=0
while x<6:
    print(list2[x],end='')
    x=x+1
x=0
list1=[]
while x<10:
    num= random.randint(1,9)
    list1.append(num) 
    x=x+1
x=0
ran=random.randint(3,8)
while x<ran:
    print(list1[x], end='')
    x=x+1
print("\n Thank You!!!") 

