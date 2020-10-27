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
def fizzbuzz(n):
    i = 1
    while i <= n:
        if i%3 == 0 & i%5 == 0:
            print('fizzbuzz')
        elif i%3 == 0:
            print ('fizz')
        elif i%5 == 0:
            print('buzz')
        else: 
            print(i)
        i+= 1
fizzbuzz(15)



#CONTROL FLOW PROBLEM 2: Multiply Without *
#Write a python function which multiplies two values (a and b) without using the multiplication symbol. Use addition and a while loop to write your function

#CONTROL FLOW PROBLEM 3: Output the first n prime numbers
#Write a python function that outputs the first n prime numbers


