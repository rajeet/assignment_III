# Quick_Sort Algorithm
def partition(sort, low, high):
    i = (low - 1)
    pivot = sort[high]

    for j in range(low, high):
        if sort[j] < pivot:
            i = i + 1
            sort[i], sort[j] = sort[j], sort[i]

    sort[i + 1], sort[high] = sort[high], sort[i + 1]
    return (i + 1)

def quickSort(sort, low, high):
    if low < high:
        pi = partition(sort, low, high)
        quickSort(sort, low, pi - 1)
        quickSort(sort, pi + 1, high)

listofnum = [5,10,20,15,12,50,55,3]
n = len(listofnum)
quickSort(listofnum, 0, n - 1)
for i in range(n):
    print("%d" % listofnum[i]),