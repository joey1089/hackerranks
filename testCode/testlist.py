# list - operations

# List Iteration (method-1):
a = ["item_0","item_1","item_2","item_3","item_4"]
# for item in a:
#     print(item)

# List Iteration (method-2):
# range(3) creates a list of [0,1,2]
# for i in range(3):
#     print(i)
# # To get the item from the list
# for i in range(len(a)):
#     print(a[i])


# >>> a = ["item_0","item_1","item_2","item_3","item_4"]
# >>> print(a[2])
# item_2
# >>> print(a)
# ['item_0', 'item_1', 'item_2', 'item_3', 'item_4']
# >>> mix = [0,1,"two","three","four"]
# >>> print(mix[2])
# two
# >>> 


# b_list = [0,0,0]
# b_list[1] = "one"
# print(b_list[1])
# print(b_list)
# b_list[2] = "two","three"
# print(b_list)
# print(b_list[2][1])

# #find the sum of e_list, which contains:[32,55,710,1]
# e_list = [32,55,710,1]
# total = 0
# for item in e_list:
#     total += item

# print("The sum of e_list is : ", total)

# find the second largest number in the list
# a = [1,3,5,4,0,2]

def second_largest(given_list):
        largest = None
        sec_large = None
        for current_no in given_list:  
            #iterate over the list of numbers - first item in the list becomes the current_no
            if largest == None: 
                largest = current_no # here we have assign current_no to largest
            elif current_no > largest:
                sec_large = largest
                largest = current_no
            elif sec_large == None:
                sec_large = current_no
            elif current_no > sec_large:
                sec_large = current_no
        return sec_large
    

            
a_list = [1,3,5,4,0,2]
print(second_largest(a_list))