def find_initial_element(nums):
    if not nums:
        return None
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right)/2
        if nums[mid] < nums[left]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            return nums[left]
    return nums[left]