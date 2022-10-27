number_count=input("Please enter how many number you going to enter: ")
if number_count.isdecimal():
    i=0
    number_list=[]
    while i<int(number_count):
        number_list.append(input("please enter a number: "))
        i += 1
    sum=0
    for number in number_list:
        sum += float(number)
    print("The average number is " + str(sum/len(number_list)))
else :
    print("The text you entered is not a number!")