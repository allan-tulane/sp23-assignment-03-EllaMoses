# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    count = iterate(parens_update, 0, mylist)
    if count != 0: # if the count is not zero at the end of the iteration there is either an unequal number of open and closed parenthesis or a closed parenthesis that does not have a corresponding open parenthesis that comes before so they are unbalanced, return false
        return False
    else: # if the counter equals zero, the parenthesis are balanced
        return True

def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    if current_output < 0: #if the count is ever negative, then there is a closing parenthesis that has no matching open parenthesis. This means that the parenthesis are unbalanced regardless of what happes after so we can stop updating the count so it remains unequal to zero
        return current_output
    elif next_input == '(':
            current_output +=1; #increase counter if ( is found
    elif next_input == ")":
            current_output -= 1 #decrease counter if ) is found
    return current_output



def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0
    

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def plus(x,y):
    return x +y

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    mapped_list = list(map(paren_map, mylist)) #this will result in a list of 1s, -1s, and zeros
    prefixes, count = scan(plus, 0, mapped_list) #this will result in a list of the counts of number of unmatched parenthesis at each index =
    min = reduce(min_f, 0, prefixes) #this find the minimum of the list of counts
    if count != 0: # if the count is not equal to zero, the parenthesis are mismatched
        return False
    else: 
        if min < 0: #if at any point the count is negative, the minimum value will be less than zero. In this case the parenthesis are mistmatched because there is a closing bracket that does not have a correspondin opening bracket
            return False
        else:  #if the count ends up being zero and the min was never negative, there are no mismatched parenthesis
            return True
    

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    if len(mylist) == 0: #no unmatched parenthesis if length is 1
        n_unmatched_left = 0
        n_unmatched_right = 0
    elif len(mylist) == 1: 
        if mylist[0] == '(': # 1 unmatched left parenthesis
            n_unmatched_left = 1
            n_unmatched_right = 0
        elif mylist[0] == ')': # 1 unmatched right parenthesis
            n_unmatched_left = 0
            n_unmatched_right = 1
        else: #no unmatched parenthesis if there are no parenthesis
             n_unmatched_left = 0
             n_unmatched_right = 0

    else:
        # divide list into 2 halves and determine number of unmatched right and left parenthesis in each half
        a = mylist[:len(mylist)//2]
        b = mylist[len(mylist)//2:]
        L1, R1 = parens_match_dc_helper(a) 
        L2, R2 = parens_match_dc_helper(b)
        if L1 == R2: # if number of unmatched left parenthesis is equal to number of unmatched right parenthesis when combined, then they are balanced
            n_unmatched_left = L2
            n_unmatched_right = R1
        else: #if they aren't balaced, sum the unbalanced parenthesis in both lists
            n_unmatched_left = L1 + L2
            n_unmatched_right = R1 + R2
    return n_unmatched_left, n_unmatched_right

    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
