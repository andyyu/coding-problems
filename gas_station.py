# Andy Yu
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Difficulty: Hard

Solution Notes:
Very naive solution - iterate over every gas station index and test if you can travel the circuit starting from that point.
O(n^2) time complexity, so pretty horrendous.

First thing to note is that if the sum of 'cost' is greater than the sum of 'gas', then we won't be able to ever travel the full circuit.
Proof of this is pretty simple, just try making any basic circuit of your own and see how this is true.

Second thing to note is that if you start at a gas station A, and just barely can't make it to gas station B (due to running out of gas),
then if you start at a gas station anywhere between A and B, you still won't be able to reach B.
Example: 
A  ->  C  ->  D  ->  E  ->  B
4  (3) 4  (5) 5  (3) 4  (7) 4
When the car gets to station E, it will have 6 extra gas. The cost of the journey from E -> B is 7, so it barely can't make it from A -> B.
No matter where you start between A and B (C, D, E), you still won't be able to make it to B. Obviously this one example is not enough to prove
this idea, but the idea is that if you can't start at a station A and make it to B because the last path to B requires too much gas, then 
it won't matter which station between A and B you start from. Since you'll be reaching that station anyway when you start from A, you'll have
at least 0+ gas when you reach that station, and if you start at the station you start with 0 gas, so you'll have either more or equal to the
same gas if you had just started at A.

Using these two ideas, we can begin to build out our solution. The basic premise of my solution is to basically eliminate the stations
we CAN'T start at, so that if we can reach the 'end' starting at a certain station and the solution is actually possible (sumgas > sumcost),
then 

O(n) time
O(1) space
'''
def can_complete_circuit(gas, cost):
  if sum(cost) > sum(gas):
    return -1
  gas_left = 0
  start_station = 0
  for i, (g, c) in enumerate(zip(gas, cost)):
    gas_left += (g - c)
    if gas_left < 0:  # can't reach the station, so we restart the start station at that point
      start_station = i + 1
      gas_left = 0
  return start_station

