# prime number in range
lower_val = int(input("enter the lower range :"))
upper_val = int(input("enter the upper range :"))

list1 = []

#print("the prime number in range are :")

for num in range(lower_val, upper_val+1):
    if num>1:

        for n in range(2, num):
            if (num % n)==0:
                break
        
        else :
            list1.append(num)
        

print(list1)
print("Total {} of prime numbers from {} to {}.".format(len(list1), lower_val, upper_val))