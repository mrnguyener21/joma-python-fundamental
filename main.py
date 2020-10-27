#my age
age = 25

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

#fucntions assignment
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
print(score(20,0,20))