print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=1
 
if answer.lower()=='yes':
    answer=input('Question 1: what is 100+100000?')
    if answer.lower()=='100100':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*2
print('Marks obtained:',mark)
print('BYE!')