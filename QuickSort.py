import random

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)
    return a

def partitionRandom(a, p, r):
    x = random.randint(p, r)
    a[x], a[r] = a[r], a[x]
    return partition(a, p, r)

def quicksortRandom(a, p, r):
    if p < r:
        q = partitionRandom(a, p, r)
        quicksortRandom(a, p, q-1)
        quicksortRandom(a, q+1, r)
    return a


a = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print("Non-random pivot sort:", quicksort(a.copy(), 0, len(a)-1))
print("Random pivot sort:    ", quicksortRandom(a.copy(), 0, len(a)-1))
