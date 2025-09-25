def moveZeroes(nums):
    write_pointer = 0
    read_pointer = 0
    n = len(nums)
    
    while read_pointer < n:
        if nums[read_pointer] != 0:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
            read_pointer += 1
        else:
            read_pointer += 1
        
    for i in range(write_pointer, n):
        nums[i] = 0

# T: O(n)            
# S: O(1)