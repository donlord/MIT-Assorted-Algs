#binary search implementation of peak finding
#peak - for n, where n-1<= n >=n+1
#if array size 2, the peak is the max

def peakfinder(array):
    first = 0
    last = len(array)-1

    while first <= last:
        mid = int((first + last)/ 2)
        #case for array with 2 elements
        if (last-first <= 1):
            if (array[first]>array[last]):
                return first
            else:
                return last

        #3+ elements remaining in the array
        if ((array[mid-1] <= array[mid]) and (array[mid] >= array[mid+1])):
            return mid
        elif (array[mid-1] > array[mid]):
            last = mid-1
        elif (array[mid] < array[mid+1]):
            first = mid+1





def main():
    intlist = []
    #input with error handling to add integers into intlist
    while True:
        intvars = input("Enter numbers to create a 1d array, q to quit")
        if (intvars == 'q' or intvars =='Q' or intvars == 'quit'):
            break
        else:
            try:
                intlist.append(int(intvars))
            except ValueError:
                print('was expecting an integer, try again')


    peak = peakfinder(intlist)
    print (intlist, 'is the current list')

    #displays the peak of the list with error handling for 0,1 elements
    try:
        if (len(intlist) == 1):
            print("There is only one element in the list:", intlist[0])
        else:
            print(intlist[peak], 'is a peak in the list')
    except TypeError:
        print("There is no peak in the list")


main()


