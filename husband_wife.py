
'''
A man goes for fishing daily and when he comes at home then his wife became happy or
sad on the basis of the fishes means if the number of fishes will be greater than all previous day's maximum fishes
then she will become happy and if fishes will be less than all the previous day's lesser fishes then she will
become sad.
now tell me how many times she bacame happy
'''
number_of_days=int(input("How many day's you want to catch fishes!"))
list_of_fishes=[]

happy=0
sad=0
for i in range(1,number_of_days+1):
    k=int(input("Enter today's fishes !"))
    if(len(list_of_fishes)>0):
        if(k>max(list_of_fishes)):
            happy=happy+1
        elif(k<min(list_of_fishes)):
            sad=sad+1
        else:
            pass
    list_of_fishes.append(k)
print(f"Fishes caught by man {list_of_fishes}.")
print(f"{happy} times his Wife becomes happy! ")