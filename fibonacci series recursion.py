# fibonacci series using recursion

def fibonacci(n):

    #check if the input is less than 0
    
    if n < 0:
        print("INVALID INPUT")

    #if n is equal to 0
    
    elif n == 0:
        return 0

    #if n is 1,2 
    
    elif n ==1 or n==2:
        return 1

    else:
        return fibonacci(n-1)+ fibonacci(n-2)


n = int(input("enter the number :"))
print(fibonacci(n))