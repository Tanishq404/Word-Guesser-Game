import random
import time

print("hello and welcome to word guessing game")
time.sleep(5)
print("HINT : name of a fruit")
time.sleep(4)
fruits = ["mango","grapes","pear","orange","peach","lemon","jackfruit","plum","apple","guawa","banana","lichi"]
c = random.choice(fruits)
print("And the lenght of it is :",len(c),"letters")
b = list(c) 
d = list(b)
e = list()
string = ""
for k in d:
    string += k
empty = ""
for n in  b:
    empty += n
for m in range(len(c)):
    e.append("_")

print(e)
guesses = 10
count = len(c)

while (guesses>0):
    guess = input("enter your letter....")
    if (guess in b ):
        count = count - 1
        t =  empty.index(guess)
        e.pop(t)
        e.insert(t,guess)
        print(e)
        if(count == 0):
         break
        print("")
        b.remove(guess)
    else:
        guesses = guesses - 1
        if(guesses== 0):
            break
        print("you have only ",guesses,"attemps left") 
 
str = ""
for k in b:
    str += k
for k in range(1):
    if(guesses == 0):
        print("you loose the game")
          
    else:
        print("congratulations you won the game")        
        print(string,"is the correct name of the fruit")
        if(10-guesses == 0):
         print("you guessed the name of fruit in you first attemp")
        else:
            print("you guessed the name of fruit in",(10-guesses),"attemps")