
# Interpolation_Search_Algorithm

def interpolationSearch(sort, x):

    (left, right) = (0, len(A) - 1)

    while A[right] != A[left] and A[left] <= x <= A[right]:

        # formula
        mid = left + (x - A[left]) * (right - left) // (A[right] - A[left])

        if x == A[mid]:
            return mid

        elif x < A[mid]:
            right = mid - 1

        else:
            left = mid + 1

    if x == A[left]:
        return left

    return -1


if __name__ == '__main__':

    listofnum = [5,10,20,15,12,50,55,3]

    key = 12

    index = interpolationSearch(listofnum, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")



# note if the array provided is uniform than interpolation search will find result in just one step 
# and if the array provided is not uniform than interpolation search will or might take longer then one step 
# to find the result