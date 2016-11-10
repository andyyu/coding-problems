"""

[2, 4, 1, 3, 0, 6, 7, 1, 2, 3, 4]
return the longest increasing subsequence
[0,1,2,3] 


"""

def longest_increasing_subsequence(nums):
    longest = [{'length': 1, 'prev': None} for _ in xrange(len(nums))]
    for i, num in enumerate(nums):
        for j in xrange(i):
            if nums[j] < num and longest[j]['length'] >= longest[i]['length']:
                longest[i]['length'] = longest[j]['length'] + 1
                longest[i]['prev'] = j
    ptr_index = longest.index(max(longest, key=lambda x: x['length']))
    subsequence = []
    while ptr_index is not None:
        subsequence.append(nums[ptr_index])
        ptr_index = longest[ptr_index]['prev']
    return subsequence[::-1]
    

if __name__ == '__main__':
    print longest_increasing_subsequence([2, 4, 1, 3, 0, 6, 7, 1, 2, 3, 4])