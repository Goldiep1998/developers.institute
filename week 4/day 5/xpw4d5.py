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

#6 COME BACK TO THIS!

# def mono_check(list_nums):
#     return (all(list_nums[i] <= A[i + 1] for i in range(len(list_nums) - 1)) or
#             all(list_nums[i] >= A[i + 1] for i in range(len(list_nums) - 1))) 

# list_nums = [1,2,3,3,5,6,7]
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

#10 Words weirdly

# num_list = [10,20]
# def common_div(num1, num2):
#     for num in range(1, num1 + 1):
#         if num1 % num == 0:
#           if num2 % num == 0:
#             num_list.append(num)
#     print(num_list)      

#11 NOT DONE

#12 Works but weirdly.

# num = 15
# def prime_check (num):
#     if num > 1:
#         for num2 in range(2,num//2):
#             if num % num2 == 0:
#                 return False
#             else:
#                 return True
#     else:
#         return False
# result = prime_check(num)
# print(result) 

#13 not done

# n_list = [1,2,2,3,4,5]
# def index_even(num_list):
#   even_list = []
#   for index in range(len(num_list)):
#       if index % 2 == 0 and index != 0 and num_list[index] % 2 == 0:
#       even_list.append(num_list[index])
#   return even_list
# even_list = index_even(n_list)
# print(even_list)

#14 NODONE

# type_list = ["hi",2]
# def type_counter(type_list):
#     numbers = 0
#     string = 0
#     boolean = 0
#     a_float = 0
#     for item in type_list:
#         if isinstance(item, int) == True:
#             numbers += 1
#         elif item.is_string == True:
#             string += 1
#         elif type(item) == "bool":
    #         boolean += 1
    #     elif type(item) == "float":
    #         a_float += 1
    # print(numbers)
