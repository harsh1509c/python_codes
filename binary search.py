pos = -1
def b_search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else :
            if list[mid] < n:
                l = mid+1
            else :
                u = mid-1
    
    return False


list1 = [0,1,2,3,4,5,6,7,8,9,10]
x = 3

if(b_search(list1,x)):
    print("found at index:", pos+1)
else:
    print("not present")