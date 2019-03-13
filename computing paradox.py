# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:39:31 2019

@author: S. V. Rajeenth
"""

N = int(input())
a= list(map(int,input().split()))
k= int(input())

com_pdox=a[k-1]

a.sort()
print (a,com_pdox)

for i in range (len(a)):
    if a[i]==com_pdox:
        print(i+1)
        break
    
        