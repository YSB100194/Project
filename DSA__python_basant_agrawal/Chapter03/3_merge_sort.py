'''Merge sort is an algorithm for sorting a list of n natural numbers in increasing order. Firstly, the 
given list of elements is divided iteratively into equal parts until each sublist contains one element, 
and then these sublist are combined to create a new list in a sorted order. This programming 
approach to problem-solving is based on the divide-and-conquer methodology and emphasizes 
the need to break down a problem into smaller sub-problems of the same type or form as the 
original problem. These sub-problems are solved separately and then results are combined to 
obtain the solution of the original problem.'''

def merge_sort(unsorted_list):  
    if len(unsorted_list) == 1:  
        return unsorted_list
    mid_point = int(len(unsorted_list)/2)   
    first_half = unsorted_list[:mid_point]  
    second_half = unsorted_list[mid_point:]  
 
    half_a = merge_sort(first_half)  
    half_b = merge_sort(second_half)  
 
    return merge(half_a, half_b)



def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
             merged_list.append(first_sublist[i])  
             i += 1  
        else:
             merged_list.append(second_sublist[j])  
             j += 1
    while i < len(first_sublist):  
         merged_list.append(first_sublist[i])  
         i += 1  
    while j < len(second_sublist):
         merged_list.append(second_sublist[j])  
         j += 1
    return merged_list  




''' creating an empty list
 a = []
 
#number of elements as input
n = int(input("Enter number of elements : "))
 
#iterating till the range
for i in range(0, n):
  ele = int(input())
#adding the element
    a.append(ele)  
 
# # # # # # # print(a)'''

# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,99))


# Range of list
x = range(3, 99, 2) # Failed if negative number means -2

for n in x:
  print(n)

a= [11, 12, 7, 41, 61, 13, 16, 14,1] # 9 odd numbers
print(merge_sort(a))
print(merge_sort(x))
