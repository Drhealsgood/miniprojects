'''
Created on 13/07/2013

@author: luke
'''
# http://projecteuler.net/problem=1
def mults_of_ns(mults=[1], limit=1000):
    """
    returns the sum of all the values that are multiples of ns up to limit
    """
    return sum(set([val for val in range(limit) for arg in mults if val%arg==0]))

# http://projecteuler.net/problem=2
def listSolve(n, maxNum=4000000):
    def __even(n):
        return n % 2 == 0
    l = [1] * 3
    total = 0
    for i in range(2, n):
        loc = i % 3
        l[loc] = l[loc-1] + l[loc-2]
        if l[loc] > maxNum: break
        if __even(l[loc]):
            total = total + l[loc]
    return total

def int_while(n, maxNum=4000000):
    def __even(n):
        return n % 2 == 0
    first = second = 1
    total = count = 0
    while count < n:
        third = first + second
        if third > maxNum: break
        if __even(third):
            total = total + third
        first = second
        second = third
    return total

def intSolve(n, maxNum=4000000):
    def __even(n):
        return n % 2 == 0
    def __generateNums(n, maxNum):
        first = second = 1
        for i in range(2, n):
            third = first + second
            if third > maxNum: break
            if __even(third):
                yield third
            first = second
            second = third
    return sum(__generateNums(n, maxNum))

#http://projecteuler.net/problem=5
def smallest_multiple(div_by):
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    even        = lambda x, y: x % y == 0
    solved      = False
    value       = 232792560
    
    def check():
        for i in range(2,div_by+1):
            res     = even(value, i)
            if res != True:
                return 0
        return value
    
    while not solved:
        res     = check()
        if res != 0:
            return res
        else:
            value += 20
            
        
        

if __name__ == '__main__':
#    print("Question One:")
#    print(mults_of_ns([3,5],limit=1000))
#    n = 100000
#    print ("\nQuestion Two:")
#    print (listSolve(n))
#    print (int_while(n))
    print(smallest_multiple(40))
