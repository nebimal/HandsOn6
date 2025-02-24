# HandsOn6

## Problem 1
[Click Me](https://github.com/nebimal/HandsOn6/blob/main/QuickSort.py)


## Problem 2
<img width="998" alt="Screenshot 2025-02-24 at 1 48 54 PM" src="https://github.com/user-attachments/assets/9428480e-313e-4b5f-98ec-393269112ca4" />

## Problem 3
```
def partition(a, p, r):    
    x = a[r]                         # O(1)                        
    i = p - 1                        # O(1)  
    for j in range(p, r):            # O(n)  
        if a[j] <= x:                # O(n)  
            i += 1                   # O(n)  
            a[i], a[j] = a[j], a[i]  # O(n)   
    a[i+1], a[r] = a[r], a[i+1]      # O(1)  
    return i + 1                     # O(1)  

def quicksort(a, p, r):  
    if p < r:                        # O(1)  
        q = partition(a, p, r)       # O(n)  
        quicksort(a, p, q-1)         # T(q-1) -> T(n/2)  
        quicksort(a, q+1, r)         # T(r-q) -> T(n/2)  
    return a                         # O(1)
```
  
T(n) = T(n/2) + T(n/2) + O(n)  
T(n) = 2T(n/2) + O(n)  
### Masters Theorem
a = 2  
b = 2  
d = 1  
"O(nlogn)"  
