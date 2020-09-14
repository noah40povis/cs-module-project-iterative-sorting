# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    #traverse through all array elements 
    for i in range(len(arr)):
        #find the minimum element in remaining unsorted array 
        min_idx = i 
        #for elment in range element-i + 1 through length of array: 
        for j in range(i+1, len(arr)):
            #if the array minimum index is greater than the arrays current element 
            if arr[min_idx] > arr[j]:
                # set the new minimum equal to this element 
                min_idx = j 
                #otherwise swap positions 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    #traverse through all array elements 
    for i in range(n-1): 
        ##range(n) also work but out loop will repeat one time more than needed 
        
        # last i elements are already in place 
        for j in range(0, n-i-1):

            #traverse the array from 0 to n-i-1 
            #swap if the element found is greater 
            #than the next element 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



    return arr

arr = [64, 34, 25, 12, 22, 11, 90] 
  
print(bubble_sort(arr))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # max <- find largest element in array 
    #initialize count array with all zeros 
    #for j <- 0 to size 
        #find the total count of each unique element and 
        #store the count at jth index in count array 
    #for i <- 1 to max 
        #find the cumulative sum and store it in the count array itself
    #for j <- size down to 1 
        #restore the elemtns to array 
        #decrease count of each element restored by 1
    max = maximum+ 1
    count = [0] * max 
    for j in arr:
        #find total count of each unique element 
        count[j] =+1 
    #rewrite my answer starting with 0 
    index = 0 

    #create a list from 0 range max so it has all 
    #the numbers that could possibly be in that list 
    for num in range(max):
        #take num_in in range of zero's array (that is indexed by the numbers in max) 
        for num_in in range(count[num]): 
            # add the number to each index accordingly 
            arr[index] += num
            #increase index size each time 
            index += 1
    return arr
