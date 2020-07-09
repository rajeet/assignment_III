# Bubble_Sort Algorithm

def bubble_sort(sort):
    l = len(sort)
    for i in range(l-1):
        for j in range(0,l-i-1):
            if sort[j] > sort[j+1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
    return sort

listofnum = [5,10,20,15,12,50,55,3]
print("Bubble Sort: \n",bubble_sort(listofnum))

