
# coding: utf-8

# In[1]:


# 1.1  Write a Python Program to implement your own myreduce() function which works exactly like Python's 
# built-in function reduce() 

# Define a function to add 2 values.
def sum(a,b):
    return a + b

# Define a custom function named as myreduce
def myreduce(func, seq):
    
# Initialize a variable 'total' to store the sum of the values.
    total=0

# Iterate the sequence and apply reduction function, return the total
    for red1 in seq:
        total = func(total, red1)
    return total

# Pass the input value and print the result.
print ("Sum on list from input using custom reduce function "   + str(myreduce(sum, [1,2,3,4])))


# This is just for referecce on how Reduce function works, this code is not related to the actual question.
from functools import reduce
x=reduce((lambda x, y: x + y), [1, 2, 3,4])
print('\nSum on list using reduce fucntion ' + str(x))


# In[7]:


# 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function 
# filter() 	
# Define a function to return true if the values is greate than zero and return flase if its less than or equal to zero.
def ispositive(x):
    if (x <= 0): 
        return False 
    else: 
        return True
    
# Define a custom function named as myfiler 
def myfilter(func, seq):

 # Initialize empty list
 result = []
 # Iterate over sequence of items in sequence and apply filter function
 for fil in seq:
    if func(fil):
        result.append(fil)
 return result

# Pass the input value and print the result.
print ("Filter positive values from input list using custom filter function "  + str(myfilter(ispositive, [-2,-1,0,1,2,3,4,5])))


# This is just for referecce on how filter function works, this code is not related to the actual question..
l=[-2,-1,0,1,2,3,4,5]
x=list(filter(lambda x: x >0, l))
print('\nFilter positive values using filter fucntion ' + str(x))


# In[3]:


# Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', 'L', ' D']
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# ['A', 'C', 'A', 'D', 'G', 'I', 'L', ' D'] - Split and store it in the list
name = "ACADGILD"
let_list = [ let for let in name ]
print ("ACADGILD = " + str(let_list))

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# Fetch the list value and iterate using range value, multiply the list value with range value
inp_list1 = ['x','y','z']
result1 = [ item*num for item in inp_list1 for num in range(1,5)]
print("['x','y','z'] = " +   str(result1))

# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# Fetch the list value and multiply the list value for range value, iterate until end of list value 
inp_list2 = ['x','y','z']
result2 = [ item*num for num in range(1,5) for item in inp_list2]
print("['x','y','z'] = " +   str(result2))

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# Fetch the list value and split the list value for range value, add starting list value with range value 
inp_list3 = [2,3,4]
result3 = [ [item+num] for item in inp_list3 for num in range(0,3)]
print("[2,3,4] = " +  str(result3))

# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# Fetch the list value and for range value, add starting list value with range value 
inp_list4 = [2,3,4,5]
result4 = [ [item+num for item in inp_list4] for num in range(0,4)]
print("[2,3,4,5] = " +  str(result4))

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# write output in cartesian logic 
inp_list5=[1,2,3]
result5 = [ (y,x) for x in inp_list5 for y in inp_list5]
print("[1,2,3] = " +  str(result5))


# In[5]:


# 3. Implement a function longestWord() that takes a list of words and returns the longest one.
# Define a function to find the words length and sort it in ascending order, print the last value which is the longest one.
def longestword(words_list):
    wordlen = []
    for n in words_list:
        wordlen.append((len(n), n))
  
    wordlen.sort()
 
    return wordlen[-1][1]
print(longestword(["Phyton", "Pandas", "Data Science", "Numpy"]))

