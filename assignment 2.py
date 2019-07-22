# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:05:14 2019

@author: JoAnne
"""

print('CPSC-51100, [Summer] [2019]')
print('NAME: David Kennedy')
print('PROGRAMMING ASSIGNMENT #2')


fh = open('C:/Users/JoAnne/Desktop/hi.url','r')

lineList = [line.rstrip('\n') for line in open('C:/Users/JoAnne/Desktop/hi.txt')]
floatList = [float(x) for x in lineList]
   
k = input("Enter the number of clusters: ")
k = int(k)
minimum = min(floatList)
maximum = max(floatList)

centroids = dict(zip(range(k),floatList[0:k]))
clusters = dict(zip(range(k),[[] for i in range(k)]))

temp = 0
minimum2 = 100
differences = []
#for x in range(k):
#    for i in range(0,9):
#            temp = abs(floatList[x] - floatList[i])
#            
#            if temp != 0:
#                differences[x].append(temp)
            
#            if temp != 0:
#                minimum = temp        
#                if minimum2 < minimum:
#                    minimum = minimum2
#                else:
#                    minimum = minimum
                
    
    
#for x in floatList:
for i in range(0,9):
    temp = abs(floatList[0] - floatList[i])
    if temp != 0:
        differences.append((i,temp))
        
minimum = min(differences[1])
       
        

