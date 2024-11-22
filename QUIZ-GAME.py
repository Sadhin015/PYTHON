print("--------------------QUIZ GAME------------------")
questions=("How many elements are in the periodic table?",
           "Which animal lays the largest eggs?",
           "What is the most abundant gas in the Earth's atmosphere?",
           "How many bones are in the human body?",
           "Which planet in the solar system is the hottest?")
options=(
         ("A.116", "B.117","C.118","D.119"),
         ("A.Whales", "B.Crocodile","C.Elephant","D.Ostrich"),
         ("A.Nitrogen", "B.Oxygen","C.Carbon-Dioxide","D.Hydrogen"),
         ("A.206", "B.207","C.208","D.209"),
         ("A.Mercury", "B.Venus","C.Earth","D.Mars")
         )
answers=["C","D","C","A","D"]
guesses=[]
score=0 
question_num=0  

for question in questions:
    print("--------------------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)
    guess=input("Enter(A, B, C, D):").upper()
    guesses.append(guess)
    
    if guess==answers[question_num]:
        score+=1 
        print("-----CORRECT ANSWER!-------")
        
    else:
        print("------WRONG ANSWER!-------")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1  
                
print("--------------------------------") 
print("------------RESULTS-------------")
print("--------------------------------")
print("Answers: ",end='')

for answer in answers:
    print(answer,end=' ')
print()                   
print("GUESSES: ",end='')

for guess in guesses:
    print(guess,end=' ')
print()

score=float(score /len(questions)*100)
print(f"Your score:{score}%")