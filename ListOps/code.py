'''
Task: Delete alternate elements of the given list, starting from index 0,
      print the list after each traversal.
Example: given list -> [1,2,3,4,5]
                o/p: [2, 4]
                     [4]
                     []
'''

nums = [3, 5, 2, 9, 101, 333, 4]
print(nums)
while nums:
    i=0
    for ele in nums:
        if i%2!=0:
            pass
        else:
            nums.remove(ele)
    print(nums)
