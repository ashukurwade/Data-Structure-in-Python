def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3
nums = [19,15,19,5,3,5,2,5]
print("Original List:")
print("nums")
print("check two appearance of 19 and at least three appearance of 5 in teh said list:")
print(test(nums))
