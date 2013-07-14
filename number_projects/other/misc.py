'''
Created on 15/07/2013

@author: luke
'''

"""
Find Cost of Tile to Cover W x H Floor – 
Calculate the total cost of tile it would take to cover a floor plan of 
width and height, using a cost entered by the user.
"""
costToCover = lambda w,h,ppm: w*h*ppm
print(costToCover(50,100,0.5))