'''Question:-You have to buy chocolates
        by the given rupees you
        can buy a chocolate in Rs.1 or you can
    exchange 3 wrappers and get 1 chocolate.
'''

rupees=int(input("Enter How many rupees do yu have ? "))
chock=rupees
rapper=0
k=1
wrapper=rupees
while(wrapper!=0):
    if(wrapper%3==0):
        chock=chock+wrapper//3
        wrapper=wrapper//3
    else:
        if(wrapper<=2):
            break
        chock=chock+wrapper//3
        wrapper=wrapper%3+wrapper//3

print(f"You can buy {chock} chocolates from Rs.{rupees}")


