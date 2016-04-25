# Andy Yu
'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?


Difficulty: Easy

Solution notes:

Digital roots. The equivalent of adding up all the digits repeatedly is the same as performing a modulo by 9.

Explanation from http://www.flyingcoloursmaths.co.uk/a-neat-number-trick-digital-roots-and-modulo-9-arithmetic/
WHY IS THE DIGITAL ROOT (NEARLY) THE SAME AS THE REMAINDER?
‘Only nearly’ is the easy one: the digital root of 189 is 9, but 189 is 0 (modulo 9). If you’re dividing, you never get a remainder equal to the number you’re dividing by! You get a 0 instead. But, luckily, 9 is the same as 0 (modulo 9).
But why should the sum of the digits give you the remainder when you divide by 9? Well… remember all that stuff you did in primary school with hundreds, tens and units? Let’s revisit that, and then you can go and play in the sandpit.
Let’s take a number like 12345. That’s the same as 1 × 10,000 + 2 × 1,000 + 3 × 100 + 4 × 10 + 5.
Now, 10 is 9 + 1; 100 is 99 + 1, and so on. So let’s rewrite:
12,345 = 1 × (9,999 + 1) + 2 × (999 + 1) + 3 × (99 + 1) + 4 × (9 + 1) + 5.
Multiply out the brackets and rearrange a bit; you get:
12,345 = (1 × 9,999 + 2 × 999 + 3 × 99 + 4 × 9) + (1 + 2 + 3 + 4 + 5).
That first bracket – I don’t know what it is and I don’t really care, except that it’s a multiple of 9 – each of the numbers added if in there is clearly a multiple of 9. The second bracket is… just the sum of the digits, which is 15 – or 6 (modulo 9). If you do a quick check, 12,345 is indeed the same as 6 (modulo 9).

O(n) time
O(1) space
'''

def add_digits(num):
  if num == 0:
    return 0
  else:
    return 1 + ((num-1) % 9)