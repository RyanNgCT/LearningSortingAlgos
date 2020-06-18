nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# define bubble_sort():
def bubble_sort(arr):
  # loop through each element in list
  for item in arr:
    # compare indexes of neighbouring elements
    for index in range(len(arr) - 1):
      if arr[index] > arr[index+1]:
        swap(arr, index, index+1)

##### test statements
print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))

"""
Code Output:
Pre-Sort: [5, 2, 9, 1, 5, 6]
Post-Sort: [1, 2, 5, 5, 6, 9]
"""
