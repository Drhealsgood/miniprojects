'''
Created on 13/07/2013

@author: luke
'''
import math

def greedy_money_exchange(denom,amount):
    i   = 0
    used= [0]*len(denom)
    while(amount>0):# go until all money gone
        # get num of that denom to use, always round down
        num     = math.floor(amount/denom[i]) 
        used[i] = num # say we've used it
        amount  = amount-num*denom[i] # set new amount
        i       = i + 1 # go to next denom
    return used
