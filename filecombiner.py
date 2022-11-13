import time

filename = input("please enter filename:")
fileA=filename+"-A.txt"
fileB=filename+"-B.txt"
fileOutput=filename+"-out.txt"

file1=open(fileA)
file2=open(fileB)
fileout=open(fileOutput,"a")


lineA = file1.readline()
lineB = file2.readline()
while lineA or lineB:
    if(lineA):
        print(lineA, end="")
        fileout.write(lineA)
        lineA=file1.readline()
        time.sleep(0.3)
    if(lineB):
        print(lineB, end="")
        fileout.write(lineB)
        lineB=file2.readline()
        time.sleep(0.3)
file1.close()
file2.close()
fileout.close()
