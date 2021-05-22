'''
WCC: February 1st, 2021
'''

# def quad_solver(a ,b, c, x):
#     return (a*x**2 + b*x + c)


# def mult_table(x):
#     table = []
    
#     for col in range(1, x+1):
#         using = []
#         for row in range (1, x+1):
#             using.append(col * row)
#         table.append(using)
        
#     return table

# print (mult_table(3))


# def queue_time(queue, processors):
#     d = {}
    
#     if processors == 1:
#                 return sum(queue)
            
#     for num in range(1 , processors + 1):  
#         d[(str(num))] = 0  
#     for num in queue:          
#         key_min = min(d.keys(), key=(lambda k: d[k]))
#         d[key_min] += num
        
#     return max(d.values())


# print(queue_time([3, 7, 5], 1)) # this will return 15 because it will take 15 units of time to complete processing the queue
# print(queue_time([3, 7, 5], 2)) # this will return 8, because the first processor will handle the 3 and 5 task which will take 8 units of time
# print(queue_time([10, 7], 3)) # this will return 10, because the longest task in 10 units
# print(queue_time([10, 8, 5, 11, 9], 2)) # this will return 22

# def queue_time(queue, processors):
    
#     pros = [0] * processors
#     for time_ in queue:
#         pros[pros.index(min(pros))] += time_
#         print(pros)
#     return max(pros)



'''
WCC: February 8th, 2021
'''


'''
Hamming Distance is a measure of how different two strings of equal length are. Hamming Distance is calculated by comparing the 
strings element by element. For any position where the two strings differ, the Hamming Distance value is increased by 1. 
This has applications in Biology, Computer Science, Encryption, and many other fields. Learn more about Hamming Distance here . 
Complete the going_HAM function below. This function takes in two strings as arguments, and returns the count of differences between the two strings.
'''
# def going_HAM(str1, str2):
#     count = 0
#     for idx in range(len(str1)):
#         if str1[idx] != str2[idx]:
#             count += 1
#     return count
    

  
# print(going_HAM("ABC", "ABC")) # should return 0
# print(going_HAM("ABC", "ABD")) # should return 1
# print(going_HAM("ABC", "EFG")) # should return 3
# print(going_HAM("10010101", "11011010")) # should return 5



'''
Complete the move_zeros function below. This function takes in a single list as a parameter and returns that list with 
all the zeros moved to the end. The list can contain boolean, integers, floats, and single characters.
'''
    
# def move_zeros(lst):  
#     new_lst = []
#     zeros = []
    
#     for k in range(len(lst)):
#         if lst[k] == 0:
#             if type(lst[k]) == int or type(lst[k]) == float:
#                 zeros.append(lst[k])
#             else: 
#                 new_lst.append(lst[k])
#         else: 
#             new_lst.append(lst[k])
           
#     return new_lst + zeros

# print(move_zeros([False,1,0,1,2,0,1,3,"a"])) # will return [False,1,1,2,1,3,"a",0,0]
# print(move_zeros([1,2,0,1,0,1,0,3,0,1])) # will return [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
# print(move_zeros([0,1,None,2,False,1,0])) # will return [1, None, 2, False, 1, 0, 0]
# print(move_zeros([False])) # will return [False]
# print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])) # will return [False]

# def move_zeros(lst):
#     for i in range(len(lst)):
#         if isinstance(lst[i], bool) and lst[i] == False:
#             lst[i] = "False"
#     zeros = lst.count(0)
#     lst = [x for x in lst if x != 0]
#     lst = [False if x == 'False' else x for x in lst]
#     for _ in range(zeros):
#         lst.append(0)
#     return lst

# def move_zeros(lst):
#     res = []
#     zeros = []
#     for el in lst:
#         if el != 0 or type(el) != int:
#             res.append(el)
#             continue
#         zeros.append(el)
#     return res + zeros
'''
When lists get incredibly long it becomes incredibly slow to search through the list. Because of this computer scientists have spent years 
developing techniques to make finding items in a long list quicker. 

Binary search is a technique used to find a specific item in a list. 
Learn more about binary search here  . 

Essentially, binary search boils down to this:
The list must be sorted  
Initially use index 0 and the last index as endpoints
Calculate the midpoint of the list (if the length is even round down)
Check the value at the midpoint
If the midpoint value is the item to find, stop and return the index of that item
If the midpoint value is larger than the item to find, set the new upper index to the midpoint
If the midpoint value is smaller than the item to find, set the new lower index to the midpoint

Repeat this process until the value is found
If the value is not in the list this function should stop when the midpoint calculation return the same value as the upper or lower index

---
Write a function called bin_search that takes two parameters. 
    The first parameter is a sorted list of items, 
    the second is an item to find in the list.

This function should return a tuple of two values, 
    first is the index of the matching item, 
    second is the number of midpoint calculation it took to find that item.

Make sure to really pay attention to the examples to understand what is going on.
'''
# def bin_search(arr, find):
#     if arr == []:
#         return "Empty List"  # edge case, take care of first
#     if find not in arr:
#         return "item not in list"  # edge case, take care of first
    
#     arr = sorted(arr)

#     counter = 1
#     start = 0
#     stop = len(arr) - 1
#     mid = int(len(arr) / 2)
#     if len(arr) % 2 == 0:
#         mid -= 1
#     if arr[start] == find:
#         return start, 0
#     elif arr[stop] == find:
#         return stop, 0

#     for count in range(1, len(arr) + 1 ):
#         mid_el = arr[mid]
#         # print(mid)
#         if mid_el == find:
#             # print("mid")
#             return mid, count
#         if mid_el > find:
#             counter += 1
#             stop = mid
#             mid = int(mid / 2)
#         if mid_el < find:
#             counter += 1
#             start = mid
#             mid += int((stop - start) / 2 )
        
 
#     return mid, counter

# def bin_search(arr, find):
#     start = 0
#     stop = len(arr) - 1

#     if arr[start] == find:
#         return start, 0

#     if arr[stop] == find:
#         return stop, 0

#     for count in range( len(arr) ):
#         mid = ( start + stop ) // 2

#         if arr[mid] == find:
#             return mid, count

#         elif arr[mid] > find:
#             stop = mid
        
#         elif arr[mid] < find:
#             start = mid

# # print( bin_search([1, 3, 5, 7, 9], 2) )             # "item not in list"
# # print( bin_search([], 2) )                          # "Empty List"
# # print( bin_search([1, 3, 5, 7, 9], 3) )             # (1, 2)
# # print( bin_search([2, 4, 6, 8, 10, 12], 10) )       # (4, 3)
# # print( bin_search([2, 4, 6, 8, 10, 12], 12) )       # (5, 0)
# # print( bin_search([1, 3, 5, 7, 9, 11, 13, 15], 1) ) # (0, 0)
# print(bin_search([*range(10000)], 5001))            # (5001, 11)  FAILS this test                
# print(bin_search([1, 3, 5, 7, 9], 3))               # (1, 1))     FAILS this test       


# def bin_search(lst, el):
#     iters = 0
#     low, high = 0, len(lst) - 1
#     while True:
#         mid = (high + low) // 2
#         if el < lst[mid]:
#             high = mid
#         else:
#             low = mid

#         if lst[low] == el:
#             return low, iters
#         elif lst[mid] == el:
#             return mid, iters
#         elif lst[high] == el:
#             return high, iters

#         iters += 1
#     raise ValueError("Item not found in list given!")


'''
WCC: February 15th, 2021
'''

'''
A common issue that comes with working with large data sets is storing the data set. This is a huge issue when working with genetic data. 
One set of genes could have millions (but more like billions or trillions) of individual pieces of data in it. Add that to how many different 
genes there could be, and it becomes clear that these data sets are massive. One trick computer scientists have come up with is storing different 
genes in different bit combinations (if you aren't familiar with bits and binary, just know that bits are a series of zeros and ones, learn more about binary here  ).
Write a program that encodes these genetic sequences into binary patters. Complete the encode that takes in a sequence of genes, and returns that sequence 
of genes encoded into binary digits. This function should encode "A" as "00", "C" as "01", "T" as "10", and "G" as "11"
'''

# def encode(seq):
#     new_seq = ''
#     for k in seq:
#         if k == 'A':
#             new_seq += '00'
#         if k == 'C':
#             new_seq += '01'    
#         if k == 'T':
#             new_seq += '10'
#         if k == 'G':
#             new_seq += '11'
            
#     return new_seq

# print(encode("ACATG")) # should return "0001001011"
# print(encode("GCAGG")) # should return "1101001111"


'''
Once you have encoded the genetic data, there needs to be a way to decode the data (someone could argue that this should be done before you encode the data). 
Complete the decode function, which takes in a sequence of bits and returns the decoded genetic sequence. 
It should decode "00" to "A", "01" to "C", "10" to "T", and "11" to "G".

'''

# def decode(bits):
#     strand = []
#     decoded = ''
#     for idx in range(0, len(bits), 2):
#         strand.append(bits[idx:idx+2])
#     for bin in strand:
#         if bin == '00':
#             decoded += 'A'
#         if bin == '01':
#             decoded += 'C'     
#         if bin == '10':
#             decoded += 'T'
#         if bin == '11':
#             decoded += 'G'
   

#     return decoded

# print(decode("00110110")) # should return "AGCT"
# print(decode("101010010001")) # should return "TTTCAC"

'''
Write a function called sort_by_direction that takes two parameters. The first parameter called seq will be a list of lists where the number of lists is equal to 
the number of items in each list. The second parameter called direc will give the direction to sort each list of lists. direc will have four possible values,
"L" which will sort each row in ascending order, "R" which will sort each row in descending order, "U" which sorts each column in ascending order, 
and "D" which sorts each column in descending order.
Note that a list of lists can be represented as rows and columns like so:
[[2, 1, 5],
 [10, 2, 8],
 [1, 7, 3]]
Look at the hint for more examples of this function and what it should return.

'''

# def sort_by_direction(inp_matrix, direc):
#     rev_flag = direc in ("R", "U")

#     if direc in ("L", "R"):
#         return [ sorted(lst, reverse=rev_flag) for lst in inp_matrix ]

#     elif direc in ("U", "D"):
#         out_matrix = [ [] for _ in range(len(inp_matrix)) ]
#         for i in range(len(inp_matrix[0])):
#             column = []
#             for lst in inp_matrix:
#                 column.append(lst[i])
#             column = sorted(column, reverse=rev_flag)
#             for idx, el in enumerate(column):
#                 out_matrix[idx].append(el)

#         return out_matrix
    
# def sort_by_direction(inp_matrix, direc):
#     rev = direc in ("R", "U")

#     if direc in ("L", "R"):
#         return [ sorted(lst, reverse=rev) for lst in inp_matrix ]

#     elif direc in ("U", "D"):
#         out_matrix = [ [] for _ in range(len(inp_matrix)) ]

#         for column in zip(*inp_matrix):
#             for idx, el in enumerate(sorted(column, reverse=rev)):
#                 out_matrix[idx].append(el)

#         return out_matrix

# example = [ [3, 6, 1]
#           , [5, 2, 2]
#           , [0, 8, 7] ]

# for column in zip(*example):
#     print(column)

# example = [[3, 6, 1], [5, 2, 2], [0, 8, 7]]
# print(sort_by_direction(example, 'L')) # should return [[1, 3, 6], [2, 2, 5], [0, 7, 8]]
# # [[1, 3, 6],
# #  [2, 2, 5],
# #  [0, 7, 8]]
# example = [[3, 6, 1], [5, 2, 2], [0, 8, 7]]
# print(sort_by_direction(example, 'R')) # should return [[6, 3, 1], [5, 2, 2], [8, 7, 0]]
# # [[6, 3, 1],
# #  [5, 2, 2],
# #  [8, 7, 0]]
# example = [[3, 6, 1], [5, 2, 2], [0, 8, 7]]
# print(sort_by_direction(example, 'U')) # should return [[5, 8, 7], [3, 6, 2], [0, 2, 1]]
# # [[5, 8, 7],
# #  [3, 6, 2],
# #  [0, 2, 1]]
# example = [[3, 6, 1], [5, 2, 2], [0, 8, 7]]
# print(sort_by_direction(example, 'D'))# should return [[0, 2, 1], [3, 6, 2], [5, 8, 7]]
# # [[0, 2, 1],
# #  [3, 6, 2],
# #  [5, 8, 7]]


'''
Bubble sort is a classic algorithm to learn in computer science (and a great interview question). 
Learn more about the algorithm here. Write a function called on_the_bubble that takes a list as a 
parameter. This function should return a tuple with the first item representing the number of swaps 
that happened to sort that list, and the second is the sorted list.

Pseudocode:
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i-1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure

another version
begin BubbleSort(list)

   for all elements of list
      if list[i] > list[i+1]
         swap(list[i], list[i+1])
      end if
   end for
   
   return list
   
end BubbleSort
'''
# def on_the_bubble(arr):
#     count = 0
#     n = len(arr)
    
#     for i in range(n):
#         swap = False

#         for k in range(0, n-i-1):
        
#             if arr[k] > arr[k + 1]:
#                 arr[k], arr[k + 1] = arr[k +1], arr[k]
#                 count += 1
#                 swap = True
#         if swap == False:
#             break
#     return count, arr


# print(on_the_bubble([2, 1, 4, 3, 1, 4, 4, 5, 3, 7, 6])) # should return (10, [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 7])


'''
WCC: February 22nd, 2021
'''

'''
A Caesar Cipher is a classic encryption technique used to encrypt strings. It works by shifting each letter some 
amount in the alphabet. For instance, if the shift amount is 2 and the letter is "a" the result will be "c". It also rotates 
around so if the shift is 2 and the letter is "y" the result will be "a". Learn more about Caesar Ciphers here  . 
Complete the caesar_cipher function below. This function takes in two parameters strng and shift, which are the string to be 
encoded and the size of the shift respectively. This function should return the encrypted string. Note that there wont be any 
spaces or numbers in the string.
'''
from string import ascii_lowercase
# def alpha_score(word):
#     return {let: int(index) for index, let in enumerate(ascii_lowercase, start=1)}


# def caesar_cipher(msg, shift):
#     encrypt = ''
    
#     for let in msg.lower():
#         # convert to number and find position
#         idx = ord(let) - ord('a')
#         # shift the index
#         new_let = (idx + shift) % 26
#         # transfer back to letter
#         encrypt += chr((new_let + ord('a')))        
#     return encrypt  
 

# print(caesar_cipher("abcdefg", 8))    #"ijklmno"
# print(caesar_cipher("hello", 20))     #"byffi"
# print(caesar_cipher("dawg", 12))      #"pmis",


'''
Write a function called valid_parentheses which checks to make sure every "(" has a matching ")". This function should 
take in a string, and return a boolean. If every "(" has a matching ")" this function should return True, if it does not, 
the function should return False.


valid_parentheses("hi(hi)()") # should return True because it is a valid set of parentheses
valid_parentheses("hi())(") # should return False because its not a valid set of parentheses
valid_parentheses(")(test") # should return False because its not a valid set or parentheses
valid_parentheses("()") # should return False because it does not have a match
valid_parenthesis(")(((()))") # should return False
'''

# def valid_parentheses(g_string):
#     count = 0
#     for el in g_string:
#         if el == "(":
#             count += 1
#         elif el == ")":
#             count -= 1
#         if count < 0:
#             return False

#     return count == 0

'''
Gnome sort is a technique that expands upon the ideas of bubble sort 
(see last weeks weekly challenge for bubble sort). 
Instead of iterating through the whole list and swapping items as they come,
Gnome sort finds an item that is out of place and iterates back through the list
and places it where it needs to be and then continues going forward through the list. 
rRead more about Gnome sort here Write a gnome_sort function that takes in a list and
returns a tuple, where the first item is the number times it looped and the second item is the sorted list.

procedure gnomeSort(a[]):
    pos := 0
    while pos < length(a):
        if (pos == 0 or a[pos] >= a[pos-1]):
            pos := pos + 1
        else:
            swap a[pos] and a[pos-1]
            pos := pos - 1
'''            
# def gnome_sort(lst):
#     count = 0 
#     i = 0
#     while i < (len(lst)):
#         if i == 0:
#             i += 1
#             count += 1
#         if lst[i] >= lst[i - 1]:
#             i += 1
#             count +=  1
#         else:
#             lst[i], lst[i-1] = lst[i -1], lst[i]
#             i  -= 1
#             count += 1
                      
    
#     return count, lst

# print(gnome_sort([91, 84, 79, 27, 37, 23, 20, 15, 63, 20])) #(84, [15, 20, 20, 23, 27, 37, 63, 79, 84, 91])
# print(gnome_sort([86, 92, 28, 22, 72, 25, 0, 31, 28, 31, 60, 59, 50, 52, 87])) # (105, [0, 22, 25, 28, 28, 31, 31, 50, 52, 59, 60, 72, 86, 87, 92])
# print(gnome_sort([87, 71, 70, 43, 44]))  #  (23, [43, 44, 70, 71, 87])   

'''
March 1st, 2021
'''

'''
Complete the divis_by_7 that returns True if the passed in number is divisible by 7 and False otherwise.
'''



def divis_by_7(num):
    return num % 7 == 0        
  
# # print (divis_by_7(7))
   


'''
Pig Latin is a made up language where the first letter of a word is moved to the end and then 'ay' is added to the end as well. 
For example the word "Hello" becomes "elloHay". Complete the pig_latin function below, which should take a string as input, 
convert every word to Pig Latin, and then return the updated string.
'''

# def pig_latin(words):
#     separated_words = words.split()
#     pig_lat = []
#     for word in separated_words:
#         if word.isalpha():
#             pig_lat.append(word[1:] + word[0] + "ay")
#         else:
#             pig_lat.append(word)
        

#     return   ' '.join(pig_lat)
    

# print(pig_latin("Hello")) # "elloHay" 
# print(pig_latin("I really like to code")) # "Iay eallyray ikelay otay odecay"
# print(pig_latin("Something clever!")) # "omethingSay clever!" notice how punctuation means the string is not converted to Pig Latin
# print(pig_latin("Numb3rs sho0ld st@y"))



'''
Write a function called first_n_smallest. 
This function should take in two parameters with the first being a list of numbers and the second being the number of items to keep 
in that list. This list should contain the n smallest integers in their original order.
'''


# def first_n_smallest(arr, n):
#     arr_sorted = sorted(arr)[0:n]
#     out = []
#     for num in arr:
#         if num in arr_sorted:
#             out.append(num)
#     return out

# print(first_n_smallest([5,4,3,2,1],3)) #   should return [3,2,1]
# print(first_n_smallest([1,2,3,-4,0],3)) #  should return [1,-4,0]
# print(first_n_smallest([2,1,2,3,4,2],4)) # should return [2,1,2,2]



'''
Write a class called Member. 
This class should take in a person's name, age, email, and password. 
These should be saved in attributes called name, age, email, and password. 
This class should also have wo additional attributes user_name and secure_pw. 
user_name should be everything before the @ symbol in 
their email and secure_pw should be a boolean that represents whether their password is longer than 16 characters for not. 
If you are not familiar with Object Oriented Programming check out these lessons from learn here  .
'''

class Member:
    def __init__(self, name, age, email, password):
        
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.user_name = (email.split('@'))[0]
        self.secure_pw = len(password) > 16
    
test = (Member('Bob', 25, 'peter@gmail.com', '10358td3d33d3derw43'))



'''
March 8th, 2021
'''


'''
Finish the complete_square function below. This takes a number, called num, and it should 
return True if that number is a perfect square and return False if the number is not a perfect 
square. Recall that a perfect square is a number that can be calculated by multiplying a number
times itself.

The value of 4 is a perfect square because 2 * 2 = 4
The value of 9 is a perfect square because 3 * 3 = 9
The value of 8 is not a perfect square because no whole number times itself gives 8

Big Hint
The square root can be calculated by raising a number to the 12 power.
'''

def complete_square(num):
    return num**(1/2) % 1 == 0
    # Write your code here
    pass
# print(complete_square(3))

def complete_square(num):
    return int(num ** (1/2)) ** 2 == num

# print(complete_square(3))
'''
Write a function called direction_handler that takes in a list of directions. This list of 
directions will contains the words 'NORTH', 'SOUTH', 'EAST', 'WEST'. These directions could 
have redundant steps, a redundant step for example would be a 'NORTH' followed directly by 
a 'SOUTH' or a 'WEST' directly followed by a 'EAST'. The goal of this function is to reduce 
these redundant steps so there is a simple set of instructions to follow at the end.

'''
redundant = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def direction_handler(lst):
    optimized_trip = []
    for dir in lst:
        if optimized_trip and optimized_trip[-1] == redundant[dir]:
            optimized_trip.pop()
        else:
            optimized_trip.append(dir)
    return optimized_trip

# print(direction_handler(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# # should return ['WEST']
# print(direction_handler(["NORTH", "WEST", "SOUTH", "EAST"]))
# # should return ["NORTH", "WEST", "SOUTH", "EAST"]


'''
Write a function called largest_sub_sum that find the largest possible continuous sub array 
sum in the given list.
'''

def largest_sub_sum(arr):
    largest = 0
    working = 0
    start_idx = 0
    stop_idx = 0 
 
    for idx, num in enumerate(arr):
        if working <= 0:
            working_start = idx
            working = num
        else: working += num
        
        if working > largest:
            largest = working
            start_idx = working_start
            stop_idx = idx + 1
        
        
    return sum(arr[start_idx : stop_idx])


def largest_sub_sum(arr):
    lst = []
    if len(arr) == 0: return 0
    for i in range(0, len(arr)):
        for j in range(len(arr), i-1, -1):
            lst.append(sum(arr[i:j]))
    return max(lst)

# print(largest_sub_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # should return 6: [4, -1, 2, 1]
# print(largest_sub_sum([5, -10, 5, 2, 7])) # should return 14: [5, 2, 7]
# print(largest_sub_sum([-5, -2, 1, 10, -4, 5, -6, 7])) # should return 13: [1, 10, -4, 5, -6, 7]
# print(largest_sub_sum([])) # should return 0: []

'''
The next few Object Oriented Programming(OOP) question are going to work to build out an object called 
a Single Linked List(SSL). Learn more about SSL here.  
SSL introduces a few important concepts to OOP. 
The first is a "node", which is a container that stores data in it. 
The second is an "edge" or "pointer", this links from one node to another and allows the programer to go from one node to another. 
Third is a "controller" which is a class that knows how to use containers to do useful things like create SLL! 
Essentially a SSL creates a list like is available in python, but it can only be moved from beginning to end.
If you are unfamiliar with OOP you can learn more about it here. 
Word of warning, these are very common data structures and a quick internet search can yield thousands of possible implementations, these can be helpful 
to learn more about OOP, but probably wont work for this question so you will need to implement it on your own.

For this challenge write two classes. 
The first class called Node will be the nodes that the link list creates and uses to make the list. 
The __init__ should take in the value to be added to the list, and create two attributes, value which will 
hold the value and nxt which will be set to None. The node should 
also have a __repr__ that returns the string "The value: <value>", where is the value in that node.
'''
class Node:
    def __init__(self, val):
        
        self.value = val
        self.nxt = None
        
    def __repr__(self):
       return   f"The value: {self.value}"
       
    
# my_node = Node('Hello')
# print(my_node)
# print(my_node.value)
# print(my_node.nxt)    


'''
The second class should be called SLL. This classes __init__ should 
create three attributes start, end, and count. 
The values should be created with values of None, None, and 0. 

After that, create a method called push that takes a single value. 
This method will create a new instance of the node and will add it to the end of the list,
it will also increment the count by 1. 

To add it to the end of the list, in the previous Node set the value of nxt to the new node. 

Finally add a show method that will print all the nodes from beginning to end of the list. 

The show method will not be tested in the final solution, but it is very helpful for debugging.
'''
class SLL:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def push(self, val):
        self.count += 1
        new_inst = Node(val)
        if self.start == None:
            self.start = new_inst
            self.end = new_inst
        else:
            self.end.nxt = new_inst
            self.end = new_inst
       

    def show(self):
        if self.start != None:
            node = self.start
            print(node)
            while node.nxt != None:
                node = node.nxt
                print(node)
        else:
            print("Empty list")   

  
    
   