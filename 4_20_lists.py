# # my_list = [1,2,3,4,5,6,7,8,9,9,0]
# # print(len(my_list))

# my_list = [10, 20, 'Jessa', 12.50, 'Emma']
# print(my_list[1])
# print(my_list[4])

# empty_list = []
# print ()

# numbers = [1,2,3,4,5]
# print(numbers)

# triples = [1,2,3]*3
# print (triples)

# aList = [100,200,300,400,500]
# aList = aList[::-1]
# print(aList,"\n")

# function to check whether

# first and last character of words match

def match_words(words):
     ctr = 0
     lst = []
     for word in words:
         if len(word) > 1 and word[0] == word[-1]:
          ctr += 1
          lst.append(word)
          
     print("List of words with first and last character same\n", lst) 
     return ctr

count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count)