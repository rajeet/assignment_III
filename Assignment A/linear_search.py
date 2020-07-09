# Linear_Search_Algorithm

def linear_search(sort, search):
    l = len(sort)
    for i in range(0, l-1):
        if sort[i] == search:
            return i
    return i

find = 12
listofnum = [5,10,20,15,12,50,55,3]
index = (linear_search(listofnum, find))
print(f"index of {find} is {index}")
