l1 = [10,45,3,4,1,79,100,45,78,12,45,101,23,50]
print(l1)
x = int(input("enter the number you want to check if it is in list or not :"))

def search(arr, x):
    for i in range(len(l1)):

        if l1[i]==x:
            #print(x, "is present at index {}".format(l1[i]))
            return i
    return -1

print(search(l1,x))