 # TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # Your code here
#     for j in range(i+1, len(arr)): 
#         if arr[smallest_index] > arr[j]: 
#             smallest_index = j 
              
#     # Swap the found smallest element with the first element         
#     arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 
    
#     return arr


def selection_sort(arr):

    # loop through n-1 elements

    for i in range(0, len(arr) - 1):

        sorted_boundary = i

        smallest_index = sorted_boundary

        # TO-DO: find next smallest element

        # (hint, can do in 3 loc)

        # Your code here

        # iterate through the unsorted portion of the array 

        # finding the index of the smallest element in the unsorted portion

        for unsorted_index in range(sorted_boundary, len(arr)):

            # if we find a value < smallest_index element,

            # update our smallest_index variable 

            if arr[unsorted_index] < arr[smallest_index]:

                smallest_index = unsorted_index

​

        # TO-DO: swap

        # Your code here

        # we've found the smallest element in the unsorted portion 

        # swap it with the element right next to the boundary 

        arr[smallest_index], arr[sorted_boundary] = arr[sorted_boundary], arr[smallest_index]

​

    return arr



# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     # Your code here
 
#     n = len(arr) 
  
#     # Traverse through all array elements 
#     for i in range(n-1): 
#     # range(n) also work but outer loop will repeat one time more than needed.   
#         # Last i elements are already in place 
#         for j in range(0, n-i-1): 
  
#             # traverse the array from 0 to n-i-1 
#             # Swap if the element found is greater 
#             # than the next element 
#             if arr[j] > arr[j+1] : d   
#                 arr[j], arr[j+1] = arr[j+1], arr[j] 

#     return arr


def bubble_sort(arr):

	# it traverses the array

    # loop until no more swaps occur 

    swaps_occurred = True

​

    while swaps_occurred:

        swaps_occurred = False 

​

        for i in range(0, len(arr)-1):

            # compare two elements 

            if arr[i] > arr[i+1]:

                # swaps them if the two elements aren't in order 

                arr[i], arr[i+1] = arr[i+1], arr[i]

                swaps_occurred = True

				

	return arr


'''
STRETCH: implement the Count Sort function below

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
    # Your code here


    return arr
