# Binary_Search_Algorithm

def binary_search(sort,left, right, search):
    

    if right >= left:
        mid = left+(right+left) //2
        if sort[mid] == search:
            return mid
        elif sort[mid] > search:
            return binary_search(sort, left, mid-1, search)
        else:
            return binary_search(sort, mid+1, right, search)
    else:
        return -1

    print(right)
    sortedsort = sorted(sort)





find = 12
listofnum = [5,10,20,15,12,50,55,3]
left = 0
right = len(listofnum)-1
result = (binary_search(listofnum, left, right, find))
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 