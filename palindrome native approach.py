# to check string is palindrome, native approach

def ispalindrome(s):
    return s == s[::-1]


s = input("enter string : ")
ans = ispalindrome(s)

if ans:
    print("yes")
else:
    print("no")
    print(s[::-1])