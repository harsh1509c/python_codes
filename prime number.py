# prime numbers
num = int(input("enter the number : "))

# if the num is greater than 1
if num> 1:
    # iterate from 2 to n/2
    for i in range(2, int(num/2)+1):
        # if num is divisible by any number between
        # 2 to num/2, it is not a prime
        if (num % i) == 0:
            print(num,"is NOT a PRIME NUMBER.")
            break
    else:
        print(num,"is a PRIME NUMBER.")

else:
    print(num, "is NOT a PRIME NUMBER.")