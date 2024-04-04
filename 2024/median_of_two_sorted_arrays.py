#!/usr/bin/env python3
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    s = sorted(nums1+nums2)
    n = len(s)
    if n%2!=0:
        return float(s[int(n/2)])
    else:
        return float((s[int(n/2)-1]+s[int(n/2)])/2)

print('-'*20)    
print(findMedianSortedArrays([1,3],[2]))
print('-'*20)
print(findMedianSortedArrays([1,2],[3,4]))
print('-'*20)