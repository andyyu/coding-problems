# Andy Yu
'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. 
This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


Difficult: Medium

Solution Notes:

First create a graph (dictionary of dictionaries) - I used defaultdict for convenience, since it will automatically create a default dict if a value is not found.
Then I just use DFS to search through the graph for the answer, avoiding loops by keeping track of path.

'''

def calculate_equation(equations, values, queries):
    # generate directed graph
  graph = collections.defaultdict(dict)  # create empty dict that will automatically create an empty default "dict" as a value if a nonexisting key in the outer dict is accessed
  for fraction, value in zip(equations, values):  # iterate over equation and value pairs
    graph[fraction[0]][fraction[1]] = value       # add edge a->b of weight value
    graph[fraction[1]][fraction[0]] = 1/value     # add edge b->a of weight 1/value
    graph[fraction[0]][fraction[0]] = 1.0         # add edge a->a of weight 1
    graph[fraction[1]][fraction[1]] = 1.0         # add edge b->b of weight 1
  return [dfs(graph, query[0], query[1], []) for query in queries] # return list of results for every query

def dfs(graph, start, end, path):
  if start in graph and end in graph: # check if both start and end nodes are in the directed graph, if not then there can't be an answer
    for node in graph[start]:         # check every node connected by an edge to the "start" node
      if node == end:                 # solution found. return the weight of that edge
        return graph[start][node]     
      if node not in path:            # check path to avoid loop
        val = dfs(graph, node, end, path+[node])  # recurse using each connected node (DFS), add node to path
        if val != -1:                 # DFS found answer
          return graph[start][node]*val   # bubble up values to top
  return -1.0  # couldn't find answer

  

