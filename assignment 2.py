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
   
#k = input("Enter the number of clusters: ")
#k = int(k)
k = 2 
'''delete'''

centroids = dict(zip(range(k), floatList[0:k]))
clusters = dict(zip(range(k), [[] for i in range(k)]))
maping = dict(zip(range(10), floatList[0:10]))

#clusters.update(0 = floatList[0])

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

        
for i in range(0,k): # set 5 to k - number of clusters
    clusters[i].append(floatList[i])   
    for ii in range(k,len(floatList)):
        temp = abs(floatList[i] - floatList[ii])
        if temp != 0:
            differences.append((ii,temp))
            differences.sort(key = lambda x: x[1])
            
            
    clusters[i].append(floatList[differences[0][0]])
    floatList[differences[0][0]] = 1000
    floatList.remove(1000)
    differences = []
    
    mean = sum(clusters[i])/len(clusters[i])
    centroids[i] = mean

#for i in range(0,k):
#    mean = sum(clusters[i])/len(clusters[i])
#    centroids[i] = mean
            
#    minimum = min(differences[1])
#    clusters[0].append(10)









    
##for x in floatList:
#for i in range(0,9):
#    temp = abs(floatList[0] - floatList[i])
#    if temp != 0:
#        differences.append((i,temp))
#        differences.sort(key = lambda x: x[1])
#        
#clusters[0].append(floatList[differences[0][0]])
#        
#minimum = min(differences[1])
#clusters[0].append(10)
