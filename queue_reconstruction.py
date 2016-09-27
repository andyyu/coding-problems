# Andy Yu
'''
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example:

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Difficult: Medium

Solution Notes:
Easiest way I thought of was to first create a dictionary (I called it height_map) that maps people as entries of key "h" and value "k".
This produces something like:
7: 0, 1
6: 1
5: 0, 2
4: 4

I then iterate over the keys in descending order (tallest first), and place them in the list. 
Since I'm going in descending order, I can be confident that no other future entries will disturb the "k" (people that are taller) of any entries I put down.
Therefore, I simply have to put each entry [h, k], in a position "k" from the front (since all taller entries will have already been inserted into the result, while any shorter won't affect the k).
Running through the algorithm by hand would produce something like:
[7,0] (Insert in ascending k order)
[7,0] [7,1] <- Insert [7,1] in index 1
[7,0] [6,1] [7,1] <- Insert [6,1] in index 1, notice how this doesn't affect the "k" of [7,1] since we're adding them in decreasing height order 
[5,0] [7,0] [6,1] [7,1] <- Insert [5,0] at index 0
[5,0] [7,0] [5,2] [6,1] [7,1] <- Insert [5,2] at index 2
[5,0] [7,0] [5,2] [6,1] [4,4] [7,1] <- Lastly, insert [4,4] at index 4

Unfortunately, even though our loop is only O(n) (don't be fooled by the nested for loop, it only ever iterates over n number of people), Python's insert() into a list is O(n).
This means our final time complexity is O(n^2). There is a better time complexity algorithm possible (O(n log n)), but it actually performs slower given the question's constraints (n < 1,100).

O(n^2) time
O(n) space
'''

def reconstructQueue(self, people):
    result = []
    height_map = collections.defaultdict(list)
    for h, k in people:
        height_map[h].append(k)
    for h in sorted(height_map.keys(), reverse=True):
        for k in sorted(height_map[h]):
            result.insert(k, [h, k])
    return result