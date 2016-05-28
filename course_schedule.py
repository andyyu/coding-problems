# Andy Yu
'''
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
So it is impossible.


Solution Notes:

We use a DFS algorithm for Topological Sort. 
We basically need to find a cycle in the graph, and if it exists, it is impossible to take every class. 
(Try drawing a simple example).

O(n) time
O(1) space
'''

def canFinish(self, numCourses, prerequisites):
  if not prerequisites: # basic check
    return True
  graph = [[] for _ in xrange(numCourses)]  # empty graph
  for pair in prerequisites:
    graph[pair[0]].append(pair[1])          # build graph based off pairs
  for i in xrange(numCourses):              # for every course in the graph, run dfs
    if not self.dfs(i, graph, []):          # dfs, if it returns False then we know there was a cycle
      return False
  return True
        
def dfs(self, start, graph, current_path):
  current_path.append(start)                # current_path keeps track of a single path, if we encounter the same node in current_path, there must be a cycle
  if not graph[start]:                      # course either has not prereqs or has been encountered already
    return True
  else:
    temp = graph[start]                     # remember prereqs
    graph[start] = []                       # 'clear' prereqs in graph to mark as encountered
    for edge in temp:                       # DFS - recursively call on every prereq
      if edge in current_path or not self.dfs(edge, graph, list(current_path)):  # check if makes cycle (in current path). If not, run dfs on it and see if it ever makes a cycle.
        return False
  return True