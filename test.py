import random

#This should be able to generate random list from the poolsize with giving numbers
def picknumbers(poolsize, ballnum):
    balls=list(range(1, poolsize+1))
    results=[]
    i=0
    while i<ballnum:
        random.shuffle(balls)
        results.append(balls.pop())
        i+=1
    return results

number_count=input("How many sets of numbers are you going to generate: ")
if number_count.isdecimal():
    j=0
    while j<int(number_count):
        print(picknumbers(35,7),picknumbers(20,1), picknumbers(7,2))
        j+=1