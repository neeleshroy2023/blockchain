import random
import math
number = math.floor(random.random() * 100)
answer = -1
while(answer != number):
    answer = int(input("take a guess: "))
    if(answer > number):
        print("Guess lower")
    elif(answer < number):
        print("Guess higher")
print("Correct answer ", answer)