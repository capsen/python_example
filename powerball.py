import random

# This should be able to generate random list from the poolsize with giving numbers
def picknumbers(poolsize, ballnum):
    balls=list(range(1,poolsize+1))
    results=[]
    i=0
    while i<ballnum:
        random.shuffle(balls)
        results.append(balls.pop())
        i+=1
    return results

num = input("How many sets of number you want to generate: ")
numcount=0
while numcount<int(num):
    print(sorted(picknumbers(35,7)), picknumbers(20,1))
    numcount+=1

