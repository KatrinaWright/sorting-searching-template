# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Recursive Binary Search
#
# NAME:         FIXME
# ASSIGNMENT:   Technical HW: Sorting & Searching

# Write a recursive function `binary_search` that
# takes an ordered array of numbers as a parameter
# and a number to search for and returns the index
# of the number in the array, or -1 otherwise. For
# full credit, the search should be implemented using
# recursion, rather than a loop.
def binary_search(array, num):
    return -1

def main():
    a = [i for i in range(-1, 10, 2)]
    print(a)
    for n in [1, 0, -1, 2, -2, 4, 5, 6, 7, -67, 134]:
        print("%5d index? %d" % (n, binary_search(a, n)) )

main()