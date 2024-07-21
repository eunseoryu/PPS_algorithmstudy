def quick_sort(nums):
    if not nums:
        return nums
    
    pivot = nums.pop()
    left = []
    right = []
    
    for num in nums:
        if num > pivot:  
            left.append(num)
        else:
            right.append(num)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

nums = list(map(int, list(input()))) 
sorted_nums = quick_sort(nums)

print(''.join(map(str, sorted_nums)))  
