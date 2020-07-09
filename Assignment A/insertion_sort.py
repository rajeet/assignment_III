# Insertion_Sort Algorithm
def insertion_sort(sort):
    l = len(sort)

    for i in range(1,l):
        key = sort[i]
        j = i-1
        while j>=0 and key < sort[j]:
            sort[j+1] = sort[j]
            j-=1
        sort[j+1] = key
    return sort

listofnum = [5,10,20,15,12,50,55,3]
print(insertion_sort(listofnum))
