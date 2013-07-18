'''
Created on 13/07/2013

@author: luke
'''
import time
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
            value += 40
            
            
# http://projecteuler.net/problem=6
def problem_six(num):
    """
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    now         = time.time()
    sum_squares = lambda value: sum([x**2 for x in range(num+1)])
    square_sum  = lambda value: (sum(range(num+1)))**2
    return(square_sum(num)-sum_squares(num), time.time()-now)

def problem_six_revisit(num):
    now         = time.time()
    sum_squares = lambda val: sum(map(lambda x: x**2, range(num+1)))
    square_sum  = lambda val: (sum(range(num+1)))**2
    return (square_sum(num)-sum_squares(num), time.time()-now)

def prob_six(num):
    now         = time.time()
    return (sum([i for i in range(1,num+1)])**2) - sum([x**2 for x in range(num+1)]), time.time()-now

def prob_six_re(num):
    now         = time.time()
    return ((sum(range(1,num+1)))**2 - sum(map(lambda x: x**2, range(1,num+1))), time.time()-now)

#http://projecteuler.net/problem=7
def problem_seven():
    """
    Generate primes - Sieve of Eratosthenes
    from http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
    too beautiful to not use
    """
    table   = {}
    value   = 2 # first prime
    
    while True:
        # does prime exist already
        if value not in table:
            # value is a new prime
            # yield it and mark its first multiple 
            # that isn't already marked
            yield value
            table[value*value]  = [value]
        else:
            # value is a composite, table[value] is the list of primes that divide it.
            for p in table[value]:
                table.setdefault(p+value,[]).append(p)
            del table[value]
        value   += 1
        
def primes_until(n):
    i       = 0
    target  = n
    y       = []
    for x in problem_seven():
        y.append(x)
        i += 1
        if i >= target: break;
    return y

#===============================================================================
# http://projecteuler.net/problem=26
#===============================================================================
def reciprocal_cycles(n):
    
    results     = {}
    # collect results
    for i in range(1,n):
        x       = 1/i
        results[len(str(x))]    = x
        

#===============================================================================
# # http://projecteuler.net/problem=29
#===============================================================================

def distinct_powers(n,m):
    return len(set([i**j for i in range(2,n+1) for j in range(2,m+1)]))

# 37
def problem_thirty_seven():
    primes  = primes_until(10001)
    
    
    def truncable(value):
        front,back     = value, str(value)[::-1]
        while True:
            if front == "": break;
            if int(front) not in primes:
                print(front)
                return False
            if int(back) not in primes:
                print(front)
                return False
            front       = str(front)[1:]
            back        = str(back)[1:]
        return True
    
    for val in primes:
        if truncable(val):
            yield val
        


            
        
        

if __name__ == '__main__':
#    print("Question One:")
#    print(mults_of_ns([3,5],limit=1000))
#    n = 100000
#    print ("\nQuestion Two:")
#    print (listSolve(n))
#    print (int_while(n))
#    print(smallest_multiple(40)
#    x = res_one, res_two, res_three, res_four = problem_six(100), problem_six_revisit(100), prob_six(100), prob_six_re(100)
#    values  = [res[0] for res in x]
#    times   = [res[1] for res in x]
#    fastest = max(times)
#    pos     = times.index(fastest)
#    print(fastest, pos)
# 26
    print(reciprocal_cycles(10))
# 29
    print(distinct_powers(100,100))
    print(3797 in primes_until(10001))
    