number_count=input("Please enter how many number you going to enter: ")
i=0
number_list=[]
while i<int(number_count):
    number_list.append(input("please enter a number: "))
    i += 1
sum=0
for number in number_list:
    sum += float(number)
print("The average number is " + str(sum/len(number_list)))