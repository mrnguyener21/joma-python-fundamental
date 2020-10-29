#my age
# age = 25

#when am i born
# print(2020 -age)

#year when it was legal to drink
# print(2020 - age + 21)

#minimum age he can date(how i met your mother)
# print(age/2 + 7)

#data types and operators
# print ( 4%3)
# print (4>=4)

#functions
def hello(name):
    greet = 'Hi ' + name
    # print(greet)
#anything indented is within the scope of the function
hello('Jonathan');

#fucntions assignment 1 SCORE
# Let's say that ever yday in joma class you get a quiz. you can eithe get the correct answer, the wrong answer or not do the quiz at all because you slept through your alarm and didn't show up to class. Each of them will have a different score:
# correct answer: 2 pts
# wrong answer: 1 pt 
# no show: 0 pt 
# write a function that produces your final score as a percentage given:
# total: the number of quizzes
# correct: the number of quizzes you answered
# wrong: the number of quizzes you answered incorrectly 
# (correct * 2 + wrong * 1) / (total * 2)
def score(total, correct, wrong):
    return ((correct * 2 + wrong * 1) / (total * 2)) * 100
# print(score(20,0,20))

#FUNCTION ASSIGNMENT 2 SCORE OF BEST 75% DAYS
# The same question as previously, however, we only take your best 75% days to account for sick days. No one is ever healthy every day. That means that even if they didn't get every question correct, as long as they got 75% of the questions correct, they will get 100%.
# write a function that produces your final score as a percentage given:
# total: the number of quizzes
# correct: the number of quizzes you answered
# wrong: the number of quizzes you answered incorrectly 

def score75(total, correct, wrong):
    return ((min((total * 0.75), correct) * 2) + min(wrong, ((total * 0.75) - min((total * 0.75), correct)))) * 100 / ((total * 2) * 0.75)



# print(score75(20,20,0))
# print(score75(20,15,0))
# print(score75(20,15,5))
# print(score75(20,10,5))
# print(score75(20,0,20))

#CONTROL FLOW IF ELSE STATEMENTS AND WHILE LOOPS
#else if() in python is 'elif' fucking gross
def can_watch_movies(age, with_parents):
    if age >= 17 or with_parents:
        return True
    else:
        return False

#while loop
# def eat_apples(num__of_apples, on_diet):
#     apples_remaining = num__of_apples
#     while apples_remaining > 0 and not on_diet:
#         apples_remaining -= 1
#         print('Thank you!')
#     print('Done')
#     return

# print(eat_apples(5, False))

#CONTROL FLOW PROBLEM 1: FIZZBUZZ
#write a pythong function with iterates the integers from 0 to n. For multiples of 3 print 'fizz' isntead of the number, and for the multiples of five, print 'buzz'. For numbers which are multiple of both three and five, print 'fizzbuzz'
# def fizzbuzz(n):
#     i = 1
#     while i <= n:
#         if i%3 == 0 & i%5 == 0:
#             # print('fizzbuzz')
#         elif i%3 == 0:
#             # print ('fizz')
#         elif i%5 == 0:
#             # print('buzz')
#         else: 
#             # print(i)
#         i+= 1
# fizzbuzz(15)



#CONTROL FLOW PROBLEM 2: Multiply Without *
#Write a python function which multiplies two values (a and b) without using the multiplication symbol. Use addition and a while loop to write your function

#CONTROL FLOW PROBLEM 3: Output the first n prime numbers
#Write a python function that outputs the first n prime numbers
#prime numbers are > 1 and can only be divided by 1 and itself
# def prime_numbers(n):
#     i = 0
#     x= []
#     while len(x) < n:
#         if i > 1 and not n % i == 0:
#             x.append(i)
#         i += 1
#         print(x);

# prime_numbers(5)
# prime_numbers(7)


#lists what are they(it's a fucking array)
nums = [2,5,14,17,20,35]
# print(nums[3])
nums [1:4] = [5,14,17] # this gives us a range


#LISTS PROBLEM 1: GENERATE LIST OF NUMBERS
# Write a python function that generates a list of numbers that starts at start and stops before end and incremnets by step 
def generate_list(start, end ,step):
    x = []
    i = start
    if step > 0:
        while i < end:
            x.append(i)
            i += step
        print(x)
        print(step)
    else:
        while i > end:
            x.append(i)
            i += step
        print(x)
    return x

# generate_list(0,5,1)
# [0,1,2,3,4] 
# generate_list(0,0,1) 
# []
# generate_list(5,10,2) 
# [5,7,9]
# generate_list(10,5,-2) 
# [10,8,6]

# LIST PROBLEM 2 : REVERSE THE LIST 
# Write a python function which reverse a list 
# note: try doing it without list.reverse(), instead try to do it with a while loops
def reverse_list(mylist):
    #while the length of the array is great than 0, remove the last element and place it into a new array
    new_array = [];
    length = len(mylist) - 1

    while length >= 0:
        new_array.append(mylist[length])
        length -= 1
    
    print(new_array)
    return new_array

# reverse_list([1,2,3,4,5])
# [5,4,3,2,1]
# reverse_list([])
# []

#LOOPS PROBLEM 1 : Is number in list?
# Write a function that checks if a numnber 'n' is in a list 'lst'
def is_in_list(n, list):
    # loop through the list
    # if list contains 'n' answer  = True else answer = False. I should probably break if n is found
    answer = False
    for i in list:
        if i == n:
            answer = True
            break

    print (answer)
    return answer
        

# is_in_list(5,[1,2,3,4])
#False
# is_in_list(5,[1,5,6])
#True

#LOOPS PROBLEM 2 : INTERSECTION OF LISTS
#Write a function intersection that consumes two lists of numbers and porduces the list of numbers that are in both lists
#AKA ARE THERE ANY NUMBERS IN BOTH LISTS
def intersection(lst1, lst2):
    answer = []
    for i in lst1:
        for j in lst2:
            if j not in answer and i == j:
                answer.append(i)
                break
    return answer
# intersection([1,2,3], [2,4,6])
# [2]
# intersection([1,2,3], [4,5,6])
# []
# intersection([2,3,2,4],[2,2,4,1,5,3])
# [2,4]

#matrix
vector = [2,3,4,5] #its a bunch of numbers bunched together. this is a 4 dimenisonal vector

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]] # a matrix is a retangular array. this is a 3x3 matrix

#MATRIX PROBLEM 1 : IS IT A VALID MATRIX?
#Write a function that determines if the given list of lists is valid, meaning that for each row, it has the same number of columns
def is_valid_matrix(matrix):
    answer = ''
    
    if len(matrix[0]) == len(matrix[1]) and len(matrix[0]) == len(matrix[2]) and len(matrix[1]) == len(matrix[2]):
        answer = True
    else: 
        answer = False

    print (answer)
    return answer

is_valid_matrix([[1,2,3],[4,5,6],[7,8,9]])
#True
is_valid_matrix([[1,2,3],[4,5],[7,8,9]])
#False


#MATRIX PROBLEM  : MATRIX MULTIPLICATION
#Write a function that multiplies two matrices together. For matrix multiplication, the number of columns in the first matrix must be equal to the number of rows in the second matrix. The result matrix, known as the matrix product, has the number of rows of the first and the number of columns of the second matrix. 

#There is a formal definition of matrix multiplication on wikipedia. https://en.wikipedia.org/wiki/Matrix_multiplication
#Output "None" if the matrices cannot be multiplied together. Use the previous function is_valid_matrix to validate the two matrices 
# before you multiply them 

# def matrix_multiply(m,n):
#     # m is the first matrix and n is the second matrix

#     return 