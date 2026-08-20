# Euler Problem 1 - Brute force v1
# Find sum of all multiples of 3 or 5 below 1000
# CIE AS: iteration + selection - you know this

def solve_bruteforce(limit=1000):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(solve_bruteforce()) # should print 233168