
# def accumulator(int=10):
#     running_total = []
#     total = 0
#     prev_num = 0
    
#     for num in range (1, int):
#         total += num
#         running_total.append(total)
        
        
#     return total, running_total
     

# total, running_total = accumulator(10)


# my_tuple = accumulator(15)

# #(45, [1, 3, 6, 10, 15, 21, 28, 36, 45])

# def item_collector(lst, itm):
#     count = 0
#     idxs = []
#     for idx, obj in enumerate(lst):
#         if obj == itm :
#             count += 1
#             idxs.append(idx)
#     return count, list(idxs)
    
# # print (item_collector([1, 2, 3, 4, 'dog', 'cat', 1, 2, 4, 4, 6, 9], 4) )  
#     # return 'number of occurences of itm, indices itm occurs
    
# # def sort_remove_dupes_print(*args):
# #     sorted_and_unique = set(sorted(args))
# #     print(" < ".join(map(str, sorted_and_unique)))

# # sort_remove_dupes_print(1, 5, 2, 3, 1, 45, 12, 4, 120, 2, 56, 6, 2, 1, 2, 4)


# def sep_and_sort(*args):
#     ints_lst = []
#     floats_lst = []

#     for arg in args:
#         if type(arg) == int:
#             ints_lst.append(arg)
#         elif type(arg) == float:
#             floats_lst.append(arg)
            
#     sort_ints = sorted(ints_lst)
#     sort_floats = sorted(floats_lst)
#     final = [sort_ints, sort_floats]
    
#     return list(filter(None, final))

# # print (sep_and_sort(1, 6, 5, 8, 4.0, 3.0, 9.0, 1.0))

# def sep_and_sort(*args):
#     separate_lists = [[], []] # list of ints, then list of floats
#     result = []

#     for elem in args:
#         if isinstance(elem, int):
#             separate_lists[0].append(elem)
#         elif isinstance(elem, float):
#             separate_lists[1].append(elem)

#     for lst in separate_lists:
#         if lst:
#             lst.sort()
#             result.append(lst)
            
#             pangram = "The quick brown fox jumps over the lazy dog"
# test = " not a pangram "
# letters = "abcdefghijklmnopqrstuvwxyz"

# def is_pangram(s):
    
#     for let in letters:
#         if let not in s.lower():
#             return False
   
#     return True
# # print (is_pangram(test))     



# def add_binary(a,b):
#     c = bin(a + b)
#     return c[2:]

# # print (add_binary(3,2))


# def find_it(seq):
#     for num in seq:
#         if seq.count(num) % 2 != 0:
#             return num
  



# # print (find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


# def min_value(digits):
    
#     no_dups = []
#     ordered = sorted(digits)
    
#     for num in ordered:
#         if num not in no_dups:
#             no_dups.append(num)
#     final = int(''.join(map(str, no_dups)))
#     return final


# # print(min_value([3,1,1]))


# def alphabet_position(text):
#     alpha = list('abcdefghijklmnopqrstuvwxyz')
#     analyze = text.lower()
#     d = {}
#     out = []
#     for idx, char in enumerate(alpha):
#         d[char]=idx+1
    
#     for char in analyze: 
#         for k, v in d.items():
#             if char == k:
            
#                 out.append(v)
#     return  ' '.join(str(num) for num in out)

# # print (alphabet_position(test))

# def square_digits(num):
#     string1 = str(num)
#     lst1 = []
    
    
#     for num in string1:
#         lst1.append(int(num)**2)
        
#         string2 = [str(num) for num in lst1]
#     return int("".join(string2))
        
        

# # print(square_digits(9119))

# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)

# def DNA_strand(dna):
#     part2 = ""
#     for idx, ele in enumerate(dna):
#         if ele == 'A':
#             part2 += 'T'
#         elif ele == 'C':
#             part2 += 'G'
#         elif ele == 'T':
#             part2 += 'A'
#         elif ele == 'G':
#             part2 += 'C'
    
#     return part2

# # print(DNA_strand('GTAT')) 

# def DNA_strand(dna):
#     match = {"A":"T","T":"A","C":"G","G":"C"}
#     return ''.join([match[nucleo] for nucleo in dna])



# def decrypt(encrypted_text, n):
#     pass


# def encrypt(text, n):
#     pass



# def find_longest(arr):
#     longest = ''
#     string = [str(num) for num in arr]
#     for num in string:
#         if len(num) > len(longest):
#             longest = num
#     return int(longest)
        
# # print(find_longest([8, 900, 500]))


# def divisors(n):
#     divisors = []
    
#     for num in range (1, n+1):
#         if n % num == 0:
#             divisors.append(num)
    
#     return len(divisors)

# # print (divisors(5))
            
            
# # def number(lines):
# #     d = {}
# #     lst = [ ]
# #     for idx, ele in enumerate(lines):
# #         d[idx + 1] = ele
# #         lst += f'{(idx+1) : ele}'
# #     return lst

# # print(number(['a', 'b', 'c', 'd', 'e']))
#     #your code here   
# # x = ['a', 'b', 'c']
# # def trst(x):
# #     out = []
# #     return  x.map {[out] out.prepend("1: ")}
# # print(trst(x))

# # number([]) # => []
# # number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]



# def queue_time(customers, n):
#     min = 0
#     for num in customers:
#         if n == 1:
#             min += num
            
#     return min

# # print (queue_time([5, 3, 4], 1))



# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the 
# # queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# # should return 12


# def multiplication_table(size):
#     final = []
    
    
#     for row in range(1, size+1):
#         series = []
#         for col in range(1, size+1):
#             series.append(row*col)

#         final.append(series)
    
#     return final
        
# # print (multiplication_table(4))        
    
# def multiplication_table(row, col):
#     final = []
    
#     for num1 in range(1, row+1):
#         series = []
        
#         for num2 in range(1, col+1):
#             series.append(num1*num2)

#         final.append(series)
    
#     return final
        
# # print (multiplication_table(3, 4))   

# '''
# size = input("Enter number: ")
# size = int(size)
 
# step = 1
# number = 1
# ran = 1
# while number < size:
#     for x in range(ran, size + 1, step)
#         print((str(ran)+"|"), x)
#         number += 1
#         ran += 1
#         step += 1       
        
        

# def main():

#     rows = int(input("Enter the number of rows that you would like to create a multiplication table for: "))
#     counter = 0
#     multiplicationTable(rows,counter)

# def multiplicationTable(rows,counter):

#     size = rows + 1

#     for i in range (1,size):
#         for nums in range (1,size):
#             value = i*nums
#             print(value,sep=' ',end="\t")
#             counter += 1
#             if counter%rows == 0:
#                 print()
#             else:
#                 counter
# '''


# def prefill(n,v):
#     out = [ ]
    
#     work = n*str(v)
#     if n == 0:
#         return []


    

#     return work
  
# # print (prefill(3, 1))  
#     #your code here
    
# def sort_array(source_array):
#     odds = []
    
#     final = []
    
#     idx = 0
    
#     for num in source_array: 
#         if num % 2 != 0:
#             odds.append(num)
#     sort = sorted(odds)
#     for num in source_array:
        
#         if num %2 != 0:
#             final.append(sort[idx])
#             idx += 1
#         else: 
#             final.append(num)
#     return final
  
        


# print(sort_array([5, 1, 2, 8, 3, 4]))  
# # [1, 3, 2, 8, 5, 4])
# print(sort_array([5, 3, 1, 8, 0]))
# #  [1, 3, 5, 8, 0])
# # test.assert_equals(sort_array([]),[])
# print(sort_array([]))

# def solution(s):
#     fixed = ''
#     for let in s:
#         if let.isupper():
#             fixed += ' '
#         fixed += let
#     return fixed

# print(solution("helloWorld"))  #, "hello World")
# print(solution("camelCase")) #, "camel Case")
# print(solution("breakCamelCase")) #, "break Camel Case")

# def find_uniq(arr):
    
    
#     for num in arr:
#         if str(arr).count(str(num)) == 1:
#             n = num
            
#     return n 
# n: unique integer in the array

# def find_uniq(arr):
    
    
#     for num in arr:
#         if arr.count(num) == 1:
#             n = num
            
#     return n 

# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))   # 2)
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))    # 0.55)
# print(find_uniq([ 3, 10, 3, 3, 3 ]))    # 10)
# def find_uniq(arr):
    
#     return [i for i in arr if arr.count(i)==1][0] # comprehension of above code


# def find_uniq(arr):
    
#     for el in set(arr):
#         if arr.count(el) == 1:
#             return el
        
# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))   # 2)
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))    # 0.55)
# print(find_uniq([ 3, 10, 3, 3, 3 ]))    # 10)       

# def find_uniq(arr):
#     return [el for el in set(arr) if arr.count(el) ==1][0]        

'''
Some new cashiers started to work at your restaurant.
They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
All the orders they create look something like this:
"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
The kitchen staff are threatening to quit, because of how difficult it is to read the orders.

Their preference is to get the orders as a nice clean string with spaces and capitals like so:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

The kitchen staff expect the items to be in the same order as they appear in the menu.

The menu items are fairly simple, there is no overlap in the names of the items:


1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke
'''

# def get_order(order):
#     cleaned = ''
#     items = ['Burger','Fries','Chicken','Pizza','Sandwich','Onionrings','Milkshake','Coke']
    
#     for ele in items:
#         if ele.lower() in order:
#             cleaned += ((ele + ' ') * order.count(ele.lower()))

#     return cleaned.rstrip()
    
# # print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))


# test = "BurgerFriesChickenPizzaPizzaPizzaSandwichMilkshakeMilkshakeCoke"

# test2 = "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke "
# test2 = test2.rstrip()
# # 

# print(test2)

# def queue_time(customers, n):
#     min = 0
#     for num in customers:
#         if n == 1:
#             min += num
            
#     return min

# print (queue_time([1, 2, 3, 4, 5], 2))



# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the 
# # queue finish before the 1st person has finished.



# def queue(queuers,pos): #still needs work
#     in_line = (len(queuers))
    
#     if pos == 0:
#         return (in_line * queuers[pos]) - (in_line - (pos + 1))
#     else: 
#         return (in_line * (queuers[pos])) - (pos + 1)
    
    
    
# print(queue([2, 5, 3, 6, 4], 0))   #6)
# print(queue([2, 5, 3, 6, 4], 1))   #18)
# print(queue([2, 5, 3, 6, 4], 2))   #12)
# print(queue([2, 5, 3, 6, 4], 3))   #20)
# print(queue([2, 5, 3, 6, 4], 4))   #17)


# def abbrev_name(name):
#     Up = []
#     first =[]
#     for let in name:
#         if (let.isupper()) == True:
#             Up.append(let)

#         # return f'{words[0]}.{words[0]}'
#     return Up

# def abbrev_name(name):
#     full = name.split()
#     first = (full[0][0]).upper()
#     second = full[1][0].upper()
       
#     return f"{first}.{second}"


# def isPalindrome(x):
#     lst = (list(str(x)))
    
#     if lst == lst[::-1]:
        
#         return True
#     return False
   
  
# print(isPalindrome(121))
# print(isPalindrome(721))
# print(isPalindrome(333))
# def duplicate_count(text):
#     dups = 0
#     low = text.lower()
    
#     for i in set(low):
#         if low.count(i) > 1:
#             dups += 1
#     return dups

# print(duplicate_count("")) #0
# print(duplicate_count("abcde")) #0
# print(duplicate_count("abcdeaa")) #1
# print(duplicate_count("abcdeaB")) #2
# print(duplicate_count("Indivisibilities")) #2

# def alpha_score(word):
#     d = {}
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     for idx, el in enumerate(alpha, 1):
#         d[el] = idx

#     score = 0
#     for letter in word:
#         score += d[letter]
        
#     return score

# def high(x):
#     words = list(x.split())
#     scores = [alpha_score(word) for word in words]

#     maxed = scores.index(max(scores))
    
#     return words[maxed]
        

# print(high('man i need a taxi up to ubud')) # 'taxi'
# print(high('what time are we climbing up the volcano')) # 'volcano'
# print(high('take me to semynak')) #'semynak'


# from string import ascii_lowercase

# def alpha_score(word):
#     return {let: int(index) for index, let in enumerate(ascii_lowercase, start=1)}


# def high(x):
#     words = list(x.split())
#     scores = [alpha_score(word) for word in words]

#     maxed = scores.index(max(scores))
    
#     return words[maxed]

# print(high('take me to semynak')) #'semynak'

# def high(x):
#     letter_worth = {letter: int(index) for index, letter in enumerate(ascii_lowercase, start=1)}
#     words = x.split()
#     total = []
#     for word in words:
#         count = 0
#         for letter in word:
#             count += letter_worth.get(letter)
#         total.append(count)
#     return words[total.index(max(total))]




# def descending_order(num):
#     string = (sorted(str(num))[::-1])
#     numish = ''
#     for ele in string:
#         numish += ele
#     return int(numish)
                
# # print(descending_order(0))# 0)
# # print(descending_order(15))# 51)
# # print(descending_order(123456789))# 987654321)


# def odd_or_even(arr):
    
#     if arr == []:
#         return 'even'
#     num_sum = 0
#     for num in arr:
#         num_sum += num
        
#     if num_sum % 2 == 0:
#         return 'even'   
#     else: return 'odd'
    
    
# # print(odd_or_even([0, 1, 2]))# "odd")
# # print(odd_or_even([0, 1, 3]))# "even")
# # print(odd_or_even([1023, 1, 2]))# "even")

# from sympy import *
# def num_primorial(n):
#     phigh = 100
#     primes = []
#     primorial = 1 
#     for num in range(2, phigh):
#         if isprime(num):
#             primes.append(num)
#     for num in primes[:n]:
#         primorial *= num
#     return len(primes)

# print(num_primorial(3))#,30)
# # print(num_primorial(4))#,210)
# # print(num_primorial(5))#,2310)
# # print(num_primorial(8))#,9699690)
# # print(num_primorial(9))#,223092870)

                
# def num_primorial(n):
#     x =100
#     primes = []
#     primorial = 1 
#     i = 0
#     for num in range(2, x):
#         if num % x == 0:
#             i += num
#         else: primes.append(num)
        
#     for num in primes[:n]:
#         primorial *= num
    
    
#     return len(primes)

  
  
  
  
   
# print(num_primorial(3))#,30)
# # print(num_primorial(4))#,210)
# # print(num_primorial(5))#,2310)
# # print(num_primorial(8))#,9699690)
# # print(num_primorial(9))#,223092870)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# primes_lst = [] 

# for n in range(2, 1000):
#     if is_prime(n) == True:
#         primes_lst.append(n)
   
# print(len(primes_lst))

# def num_primorial(n):
  
#     primes = primes_lst
#     primorial = 1 
        
#     for num in primes[:n]:
#         primorial *= num
    
    
#     return primorial

# print(num_primorial(3))#,30)
# print(num_primorial(4))#,210)
# print(num_primorial(5))#,2310)
# print(num_primorial(8))#,9699690)
# print(num_primorial(9))#,223092870)

# def num_primorial(n):
#     primorial, x, n = 2, 3, n-1
#     while n:
#         if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
#             primorial *= x
#             n -= 1
#         x += 2
#     return primorial

# def multiply_all(arr, n):
#     new_arr =[]
#     for num in arr:
#         new_arr.append(num * n)
        
#     return new_arr


# print(multiply_all([1, 2, 3],1))# [1, 2, 3])
# print(multiply_all([1, 2, 3], 2))# [2, 4, 6])
# print(multiply_all([1, 2, 3], 0))# [0, 0, 0])
# print(multiply_all([] , 10))#  []  "should return an empty array")



# def multiply_all(arr, n):
#     return[num * n for num in arr]

# print(multiply_all([1, 2, 3],1))# [1, 2, 3])
# print(multiply_all([1, 2, 3], 2))# [2, 4, 6])
# print(multiply_all([1, 2, 3], 0))# [0, 0, 0])
# print(multiply_all([] , 10))#  []  "should return an empty array")

# def lottery(s):
#     nums = ''
#     for i in s:
#         if i in '0123456789':
#             if i not in nums:
#                 nums += i
#     return nums or "One more run!"
        
# print(lottery("wQ8Hy0y5m5oshQPeRCkG")) # "805"

# print(lottery("ffaQtaRFKeGIIBIcSJtg")) # "One more run!"


# def transform(s):
#     string =''
#     for el in s:
#         string += el
#     return string
    
# print(transform(['Geeks', 'for', 'Geeks']))


'''
String#six_bit_number?, which should return true if given object is a number 
representable by 6 bit unsigned integer (0-63), false otherwise.

It should only accept numbers in canonical representation, so no leading +, 
extra 0s, spaces etc.
'''


def six_bit_number(n):
    if n == '':
        return False

    if n[0] == '0' and len(n) > 1:
            return False 
        
    elif n.isdigit() and int(n) >= 0 and int(n) < 64:
        return True 
        
    else:
        return False 
   
# print(six_bit_number(""))  # False),
# print(six_bit_number("0")) # True),
# print(six_bit_number("00"))# False),
# print(six_bit_number("55"))# True),
# print(six_bit_number("63"))# True),
# print(six_bit_number("64"))# False),
# print(six_bit_number("-0"))# False),
# print(six_bit_number("-5"))# False),
# print(six_bit_number("05"))# False),
# print(six_bit_number("5")) # True)


'''
Implement String#eight_bit_number?, which should return true if given object is a 
representable by 8 bit unsigned integer (0-255), false otherwise.

It should only accept numbers in canonical representation, so no leading +, 
extra 0s, spaces etc.

'''
def eight_bit_number(n):
    return n in map(str, range(0, 255 + 1))

# print(eight_bit_number(""))    # False),
# print(eight_bit_number("0"))   # True),
# print(eight_bit_number("00"))  # False),
# print(eight_bit_number("55"))  # True),
# print(eight_bit_number("042")) # False),
# print(eight_bit_number("123")) # True),
# print(eight_bit_number("255")) # True),
# print(eight_bit_number("256")) # False),
# print(eight_bit_number("999")) # False),
# print(eight_bit_number("-1"))  # False)

# def is_vowel(s): 
    
#     return s.lower() in 'aeiou' and len(s) == 1

# print(is_vowel('A'))
# print(is_vowel(''))   
# print(is_vowel('e'))
# print(is_vowel('ou'))



# def is_digit(n):
#     return n.isdigit() and len(n) == 1



# print(is_digit(""))#False)
# print(is_digit("7"))# True)
# print(is_digit(" "))# False)
# print(is_digit("a"))# False)
# print(is_digit("a5"))# False)


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [el for el in birds if el not in geese]

# print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])) #["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
# print(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])) #["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
# print(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"])) #[]\\\
    
'''  
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''

def spin_words(sentence):
    words = sentence.split()
    new = ''
    for word in words:
        if len(word) > 4: 
            new += (word[::-1]+ ' ')
        else:
            new += word +' ' 
    return new.strip()
    # return str([word[::-1] if len(word) > 4 else word for word in sentence.split()])
    
    
    
# print(spin_words("Hey fellow warriors")) #"Hey wollef sroirraw" 
# print(spin_words("This is a test"))      #"This is a test" 
# print(spin_words("This is another test")) #"This is rehtona test"


'''
You have a list of integers. The task is to return the maximum sum of the elements 
located between two negative elements, or -1, Nothing, or a similar empty value, 
if there is no such sum. No negative element should be present in this sum.
'''

def max_sum_between_two_negatives(arr):
    res = []
    for i, n in enumerate(arr):
        if n < 0:
            region_sum = 0
            for m in arr[i+1::]:
                if m < 0:
                    res.append(region_sum)
                    break
                else:
                    region_sum += m
            

    return max(res) if len(res) > 0 else -1


my_lst = [26, -5, 6, 4, 7, -8, 7, 20, -3, 5]
print(max_sum_between_two_negatives(my_lst))

my_lst = [30, 26, -5, 6, 4, 7, -8, 7, 20, -3, 5, 40]
print(max_sum_between_two_negatives(my_lst))

# ("between -1 and -2 there are 6, and between -1 and -2 there are 3 and 5, so return 8")
# print(max_sum_between_two_negatives([-1,6,-2,3,5,-7]))
        
# # ("between -1 and -2 there are no elements, so return 0")
# print(max_sum_between_two_negatives([5,-1,-2]))
        
# ("there are only one negative elements, so return -1")
# print(max_sum_between_two_negatives([1,-2]))
def max_sum_between_two_negatives(array):
    active = False
    max_sum = -2
    current = 0
    for number in array:
        if number < 0:
            if active:
                max_sum, current = max(max_sum, current), 0
            else:
                active = True
        else:
            current += number * active
    return max(max_sum, -1)

def max_sum_between_two_negatives(arr):
    idxs = [i for i, x in enumerate(arr) if x < 0]
    return max((sum(arr[i+1:j]) for i, j in zip(idxs, idxs[1:])), default=-1)


'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether 
the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, 
that the elements in b are the elements in a squared, regardless of the order.
'''



def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

def comp(array1, array2):
    if None not in (array1, array2): 
        a3 = [num**2 for num in array1]
        return sorted(a3) == sorted(array2)
    else: return False



# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2)) # True)
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2)) #False)
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
# print(comp(a1, a2)) #False)	


def validate_usr(user):
  return 3 < len(user) < 17 and all(c in 'abcdefghijklmnopqrstuvwxyz_0123456789' for c in user)

# print(validate_usr('hxk6Pw49rar8b6'))# True)
# print(validate_usr('aa'))# False)
# print(validate_usr('Hass'))# False)
# print(validate_usr('Hasd_12assssssasasasasasaasasasasas'))# False)
# print(validate_usr(''))# False)
# print(validate_usr('____'))# True)
# print(validate_usr('012'))# False)
# print(validate_usr('p1pp1'))# True)
# print(validate_usr('asd43 34'))# False)
# print(validate_usr('asd43_34'))# True)


'''
Number of trailing zeros of N!
'''
from math import factorial
def zeros(n):
    count = 0
    for ele in reversed(str(factorial(n))):
        if ele == '0':
            count += 1
        else: break
    return count

    


print(zeros(0))  # 0
print(zeros(6))  # 1
print(zeros(30)) # 7
print(zeros(12)) # 2
print(zeros(1000)) # ?249?


# def zeros(n):
#     return 0 if n < 5 else n/5 + zeros(n/5)

'''
Alyosha Popovich (Russian folk hero) stroke his sharp sword and cut the head of Zmey Gorynych 
(big Serpent with several heads)! He looked - and lo! - in its place immediately new heads appeared, 
exactly n. He stroke again, and where the second head was, 2*n heads appeared! 
The third time it was 2*3*n new heads, and after fourth swing it was 2*3*4*n heads, and so forth. 
And thus Alyosha decided to call it a day, and instead called a fellow Mage for help. While the Mage 
agreed, he needs to know the exact number of heads that Zmey Gorynych now has.


initial = 5
multiplier = 10
swings = 3

result:
  10 heads appearead after the first swing: 5 - 1 + 10 = 14
  20 heads appearead after the second swing: 14 - 1 + 2 * 10 = 33
  60 heads appearead after the third swing: 33 - 1 + 2 * 3 * 10 = 92
  Zmey has 92 heads in the end
'''

# def count_of_heads(initial, n, swings):
#     heads = 0
#     mult = 1
   
   
#     for num in range(1, swings+1):
#         heads = (initial-1 + (num * mult * n))
#         initial = heads
#         mult *= num
#     return heads
    
# print(count_of_heads(2, 1, 1))#,     2
# print(count_of_heads(5, 10, 3))#,    92
# print(count_of_heads(5, 10, 2))#,    33
# print(count_of_heads(51, 6, 31))#,   50983496835888389711611599965641898
# print(count_of_heads(30, 12, 31))#,  101966993671776779423223199931283755
# print(count_of_heads(10, 8, 3))#,    79
# print(count_of_heads(1, 1, 3))#,     7
# print(count_of_heads(100, 143, 8))#, 6611411

# def count_of_heads(ini, n, sw):
#     x = 1
#     for i in range(1, sw+1):
#         x *= i
#         ini = ini - 1 + x * n
#     return ini


def sum_arrays(array1,array2):
    if not array1 and not array2:
        return []
    else:
        n1 = int("".join(map(str,array1))) if array1 else 0
        n2 = int("".join(map(str,array2))) if array2 else 0
        nT = n1+n2
        lst = list(map(int,str(abs(nT))))
        if nT < 0:
            lst[0] = -lst[0]
        return lst 
    

def sum_arrays(l1, l2): # Needs work
    if l1 + l2 == []: return []
    if l1 != []:
        sl1 = int(''.join(str(i) for i in l1))
    else: 
        return l2
    if l2 != []:
        sl2 = int(''.join(str(i) for i in l2))
    else: 
        return l1

    is_neg = False
    res = []
    for n in str(sl1 + sl2):
        if is_neg:
            is_neg = False
            res.append(int(n)*-1)

        elif n == "-":
            is_neg = True
            continue

        else:
            res.append(int(n))

    return res















