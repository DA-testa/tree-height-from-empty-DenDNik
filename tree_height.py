# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    # Your code here
    tree = []
    for i in range(n):
        tree.append([])
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    def findH(node):
        heihgt=0
        for ch in tree[node]:
            heihgt = max(heihgt, findH(ch))
        return heihgt+1
    return findH(root)


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    choice = input()
    if (choice=="F"):
        lines = open("./test/"+str(input()),"r").readlines()
        n = int(lines[0])
        parents = list(map(int, lines[1].split()))
    else:
        n = int(input())
        parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))