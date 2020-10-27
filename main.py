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



print(score75(20,20,0))
print(score75(20,15,0))
print(score75(20,15,5))
print(score75(20,10,5))
print(score75(20,0,20))

#control flow
