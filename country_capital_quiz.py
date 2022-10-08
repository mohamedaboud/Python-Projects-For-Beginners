print('Welcome To Counrty Capital Quiz')
print('This quiz has 5 questions, Each is 1 point')

start= input('Do you want to start a quiz game? (y/n)')

if start.lower() != 'y':
    print('Thanks, waiting you soon')
    quit()

print('Let\'s Begin')

# initial score 
score=0

# questions
q1='What is te capital of Egypt?'
q2='What is te capital of Palastine?'
q3='What is te capital of Turkey?'
q4='What is te capital of Saudi Arabia?'
q5='What is te capital of Emirates?'

# get answers from users for each question
answer = input(q1)
if answer.lower() == 'cairo' :
    score+=1
    print('Correct!, Your score is ', score)
else:
    print('Worng answer, Your score is ', score)

answer = input(q2)
if answer.lower() == 'al quds' or answer.lower() == 'alquds' or answer.lower() == 'quds':
    score+=1
    print('Correct!, Your score is ', score)
else:
    print('Worng answer, Your score is ', score)

answer = input(q3)
if answer.lower() == 'istanbul' :
    score+=1
    print('Correct!, Your score is ', score)
else:
    print('Worng answer, Your score is ', score)

answer = input(q4)
if answer.lower() == 'al reyadh' :
    score+=1
    print('Correct!, Your score is ', score)
else:
    print('Worng answer, Your score is ', score)

answer = input(q5)
if answer.lower() == 'dubai' :
    score+=1
    print('Correct!, Your score is ', score)
else:
    print('Worng answer, Your score is ', score)

# final result
print('Your final Score is ', score, 'Ponts, ' , (score/5)*100, '%')
