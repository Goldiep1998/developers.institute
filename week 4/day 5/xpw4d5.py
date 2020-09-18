# #XP

# #1

# def find_max(num_list):
#     max_num = num_list[0]
#     for num in num_list:
#         if num > max_num:
#             max_num = i
#     return(max_num)
 
#2  

# num = int(input("Please type one number. "))
# def fact_num(num):
#   fact_list = []
#   for i_num in range(1, num + 1):
#       if num % i_num == 0:
#           fact_list.append(i_num)
#   return (fact_list)
# facts = fact_num(num)
# print(facts)



#3

# def my_sum(nums_list):
#     total = 0
#     for num in nums_list:
#         num2 = int(num)
#         total =+ num2
#     return(total)

#4

# def list_count(l_list, letter):
#     count = 0
#     for let in l_list:
#         if let == letter:
#             count += 1
#     return(count)

#5

# import math 
# def sqaure():
#     my_list = input("Enter list of numbers with comma between each number")
#     num_list = my_list.split(',')
#     sum = my_sum(num_list)
#     sqaured = math.sqrt(sum)
#     print(sqaured)
# sqaure()

#6 

# list_nums = [2,3,3,5,7,7,8]
# def mono_check(list_nums):
#     return (all(list_nums[i] <= list_nums[i + 1] for i in range(len(list_nums) - 1)) or
#             all(list_nums[i] >= list_nums[i + 1] for i in range(len(list_nums) - 1))) 


# results = mono_check(list_nums)
# print(results)


#7

# def palidrome(word):
#     r_word = word[::-1]
#     if r_word == word:
#         return True
#     else:
#         return False    

#8

# sentence = input("Please type a sentence. \n") 
# k = int(input("Please type a number. \n"))
# def k_words(sentence,k):
#     k_list = []
#     sentence = sentence.split(" ")
#     for words in sentence:
#       count = 0
#       for let in words:
#         count += 1
#         if count == k:
#           k_list.append(words)
#     return (k_list)
# counter = k_words(sentence,k) 
# print(counter)
    
#9 

# def dict_avg(num_dict):
#     values = num_dict.values()
#     sum = 0
#     for num in values:
#         sum += num
#     results = sum/len(num_dict)
#     return(results)

#10 


# def common_div(num1, num2):
#     num_list= []
#     for num in range(1, num1 + 1):
#         if num1 % num == 0 and num2 % num == 0 and num != 1:
#             num_list.append(num)
#     print(num_list)     
# common_div(10,20)     

# 11 

# def lbsearch(search_list, char, lb):
#     if lb == 'linear':
#         for chars in range(len(search_list)):
#             if search_list[chars] == char:
#                 return chars
#         return -1


#     elif lb == 'binary':
#         first = 0
#         last = len(search_list)-1
#         index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if search_list[mid] == char:
#             index = mid
#         else:
#             if char<search_list[mid]:
#                 last = mid -1
#             else:
#                 first = mid +1
#     return index

# print(lbsearch([1,2,50,74],50,'linear'))
# print(lbsearch([1,2,50,74],74,'binary'))

#12 

# num = 15
# def prime_check (num):
#     if num > 1:
#         for num2 in range(2,num):
#             if num % num2 == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False
# result = prime_check(num)
# print(result) 


#14


# def type_counter(**kwargs):
#     numbers = 0
#     string = 0
#     boolean = 0
#     a_float = 0
#     for item in kwargs.values():
#         if isinstance(item, int) == True and not isinstance(item, bool):
#             numbers += 1
#         if isinstance(item, str)== True:
#             string += 1
#         if isinstance(item, bool) == True:
#             boolean += 1
#         if isinstance(item, float) == True:
#             a_float += 1

#     return numbers, string, boolean, a_float

# result = type_counter(a=1,b='string',c=1.0,d=True,e=False)

# print(result)
