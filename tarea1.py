import random

def mergesort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        mergesort(left)
        mergesort(right)

        i=j=k=0
        while(i<len(left) and j<len(right)):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

def bubblesort(nums): 
    n = len(nums) 
    for i in range(n-1):  
        for j in range(0, n-i-1):  
            if nums[j] > nums[j+1] : 
                nums[j], nums[j+1] = nums[j+1], nums[j] 

def selectionsort(nums):
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i+1, len(nums)-1):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

def printList(lis):
    for i in range(len(lis)):
        print(lis[i], end=" ")
    print()

def listrandom(lislen):
    nums=[0]*lislen
    for i in range(len(nums)):
        nums[i] = random.randint(0,1000)
    return nums

arr = listrandom(10)
printList(arr)
selectionsort(arr)
printList(arr)