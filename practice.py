
# def factorial(num):
#     prod = 1
#     for n in range(1, num+1):
#         prod *= n
#     return prod


# def combinations(n, k):
#     return int(factorial(n) / ((factorial(n-k) * factorial(k))))



# def binomial_pmf(n, k, p=0.5):
#     return combinations (n,k) * (p**k)  * (1-p)**(n-k)

# # print (binomial_pmf(14, 12, p=0.95))


# # parallel lists and dictionaries
# import string

# x= [1,2,3,4,5,6]
# y= ['a','b','c','d','e','f']

# def number_alpha():
#     alpha = string.ascii_lowercase
#     alpha2 = []
#     nums = []
#     for num, let in enumerate(alpha, 1):
#         alpha2.append(let)
#         nums.append(num)
        
#     return alpha2, nums      
# # print(number_alpha())  

 
# alph, nums = number_alpha()
 
# # for i in range(len(alph)):
# #     print(alph[i], nums[i])    
    
# def number_alpha():
#     alpha = string.ascii_lowercase
#     d = {}
    
#     for num, let in enumerate(alpha, 1):
#         d[let] = num
   
#     return d   
 
# # print(number_alpha())  []


# # Synthesize Binary

# def create_4_bit_binary():
#     bin_list = []
    
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):
#                 for l in range(2):
#                     bin_list.append([i,j,k,l])
                    
#     return bin_list
# # print(create_4_bit_binary())

# # for lst in create_4_bit_binary():
# #     print(lst)
    
# # Analyze Binary

# bin_list = create_4_bit_binary()

# def binary_dec_dict(bin_list):
#     d = {}
#     for dec, binary in enumerate(bin_list):
#         d[dec] = binary
        
#     return d

# bin_d = binary_dec_dict(bin_list)

# # for k, v in bin_d.items():
# #     print(f'{k}:\t{v}')
    

# # Sampling approach

# def binary_dict(bin_list):
#     d = {}
#     for binary in bin_list:
#         sum_ = sum(binary)
#         if sum_ not in d:
#             d[sum_] = 0
#         d[sum_] += 1
#     return d

# bin_d = binary_dict(bin_list)

# # for k, v in bin_d.items():
# #     print(f"{k}:\t{'*'* v}") # theoretical distribution
    
from random import choice

def create_binary_list(length):
    seq = [0,1]
    bin_list = []
   
    for i in range(length):
       bin_list.append(choice(seq))
    return bin_list

# print(create_binary_list(4)) 
    
def binary_samples(num_samples=16, length=4):
    bin_samps = []
    for i in range(num_samples):
        bin_samps.append(create_binary_list(length))
        
    return bin_samps

# print(binary_samples())

bin_d = binary_samples()    

def binary_dict(bin_list):
    d = {}
    for binary in bin_list:
        sum_ = sum(binary)
        if sum_ not in d:
            d[sum_] = 0
        d[sum_] += 1
    return d

bin_d = binary_dict(binary_samples(num_samples=10000, length=8))

for k, v in sorted(bin_d.items()):
    print(f"{k}:\t{v}") 




 