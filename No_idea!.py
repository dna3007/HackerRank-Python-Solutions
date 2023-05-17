"""
input:
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

output:
Output a single integer, your total happiness.
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for e in arr:
    if e in A:
        happiness += 1
    elif e in B:
        happiness -= 1
print(happiness)
