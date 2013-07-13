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
        
def dynamic_money_exchange(denom,amount):
    """
    this is buggy
    @todo: fix the bugginess
    @param denom:     takes a bunch of denominators
    @param amount:    amount to build in denominators
    @return:          tuple(amountofcoins,whichcoins)
    """
    table       = [[0 for i in range(amount+1)] for i in range(len(denom))] # construct table
    table[0]    = range(amount+1)                                           # set value table
    used        = [0 for val in denom]                                      # used denoms
    for i in range(1,len(denom)): # go over denoms
        for j in range(0,amount+1):  # for each value up to amount
            if j < denom[i]:         # if the value is less than the denom
                # set denom i position j to the value in the previous denom at position j
                table[i][j] = table[i-1][j]
            else:
                values = (table[i-1][j], 1 + table[i][j-denom[i]])
                table[i][j] = min(values)
    print(table)
    return table[-1][-1]
        

if __name__ == '__main__':
    print(greedy_money_exchange([10,5,1],12))
    print(greedy_money_exchange([10,5,1],56))
    print(greedy_money_exchange([10,6,1],12)) # obviously [0,2,0] more appropriate
    print(dynamic_money_exchange([10,6,1],12))
    print(dynamic_money_exchange([10,5,1],12))
    print(dynamic_money_exchange([10,5,1],56))