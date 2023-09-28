# fibonacci series DP(Dynamic Programming)

# fun for the nth fibonacci number
fibary = [0,1]

def fibonacci(n):

    #check if the n is less than 0
    if n < 0:
        print("INCORRECT NUMBER")
    
    # if n is less than len(fibary)
    elif n < len(fibary):
        return fibary[n]
    
    else :
        fibary.append(fibonacci(n-1) + fibonacci(n-2))
        return fibary[n]
    
print(fibonacci(9))