# unit standard as91883 - as91884. Created by Charlotte Entwisle-Phillips, Started on 10/5/2022. My goal is to make a te reo quiz.
#https://replit.com/@Charlotte20078/test#main.py......https://replit.com/@reiman/Python-Challenge-The-Quiz#main.py

#purpose of code is to create a quiz while being funtional and good/easy to understand

#this part of code should send them to q2 or wrong depending on input v6
#this is gonna make my work look *FABULOUS* (greens my favorite colour)
score = 0

def q1():
  print ("\n"
         "Question 1")
  colour = input ("Whero is what color? \n"
                  "A.Blue \n"
                  "B.Green \n"
                  "C.Red \n"
                  "D.Yellow \n")
  colour = colour.lower()
  if colour == "red":
    print ("Correct")
    q2()

  elif colour == "C":
    print ("Correct")
    q2()
  elif colour == "c":
    print ("Correct")
    q2()
  else:
    print ("Wrong")
    q2()
  
    
    
#ask question 2, this part of code should send them to q3 or wrong depending on input v3
def q2():
  print ("\n"
         "Question 2") 
  dance = input ("What is the traditional maori dance called? \n" 
                 "A.Pukana \n" 
                 "B.Haka \n"
                 "C.Kabuki \n" 
                 "D.Taki \n")
  dance = dance.lower()
  if dance == "haka":
    print ("Correct")
    q3()
    
  elif dance == "B":
    print ("Correct")
    q3()
  elif dance == "b":
    print ("Correct")
    q3()
  else:
    print ("Wrong")
    q3()

#ask question 3, this part of code should send them to q4 or wrong depending on input v3
def q3():
  print ("\n"
         "Question 3") 
  song = input("Fill in the blank for the song - One day a ____ went swimming in the moana. \n" 
               "A.Taniwha \n" 
               "B.Mokopuna \n" 
               "C.Tuna \n")
  song = song.lower()
  if song == "taniwha":
    print ("Correct")
    q4()
  
  elif song == "A":
    print ("Correct")
    q4()
  elif song == "a":
    print ("Correct")
    q4()
  else:
    print ("Wrong")
    try_again3()

def try_again3():
  respo = input ("This was a hard question would you want to try again? [yes/no] \n")
  respo = respo.lower()
  if respo =="yes":
    q3()
  else:
    q4()
#ask question 4, this part of code should send them to q5 or wrong depending on input  v3
def q4():
  print ("\n"
  "Question 4") 
  ocean = input("What is the maori word for ocean? \n"
               "A.Wai \n"
               "B.Moana \n")
  ocean = ocean.lower()
  if ocean == "moana":
    print ("Correct")
    q5()

  elif ocean == "B":
    print ("Correct")
    q5()
  elif ocean == "b":
    print ("Correct")
    q5()
  else:
    print ("Wrong")
    q5()
#ask question 5, this part of code should send them to q6 or wrong depending on input v3
def q5():
  print ("\n"
  "Question 5") 
  word = input ("Niu Tireni is the Māori word for New Zealand \n"
               "A.True \n"
               "B.False \n")
  word = word.lower()
  if word == "false":
    print ("Correct")
    q6()
     
  elif word == "B":
    print ("Correct")
    q6()
  elif word == "b":
    print ("Correct")
    q6()
  else:
    print ("Wrong")
    q6()
#ask question 6, this part of code should send them to correct or wrong depending on input v4
def q6():
  print ("\n"
  "Question 6")
  store = input("What would be stored in a Paataka? \n"
                "A.Pukapuka \n"
                "B.Kai \n"
                "C.Waka \n")
  store = store.lower()
  if store == "kai":
    print ("Correct")
    correct()
      
  elif store == "B":
    print ("Correct")
    correct()
  elif store == "b":
    print ("Correct")
    correct()
  else:
    print ("Wrong")
    try_again6()

def try_again6():
  respo = input ("This was a hard question would you want to try again? [yes/no] \n")
  respo = respo.lower()
  if respo =="yes":
    q6()
  else:
    wrong()
#if a answer is wrong v2
def wrong():
  print ("\n"
         "Sorry that answer was wrong, please try to answer this quiz again. Good luck!!")
  

#if all answers are correct v3
def correct():
  print ("\n"
         "You got them all correct! Ka pai " + user + "\n" 
         "(っ◔◡◔)っ ♥ you're amazing ♥ \n")

#IDK WTF IM DOINGGGGGGGGGGGGGGGGG
questions_answered = 0
correct_questions = 0 
wrong_questions = 0 

question_results = [ "point", "no point"]
for item in question_results:
  questions_answered += 1

  result = item
  # iffffffffffff resulttttttttttttttttbahalabhallll https://www.youtube.com/watch?v=j1VkAGssvUg
  

#this is gonna make my work look *FABULOUS* 
print("\033[1;36m ")
#this is the intro, welcome the user explain the quiz. this is version3. dates edited/made 9/5/22 11/5/22 12/5/22
print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = input ("Hello, What is your name? ") 
print ("Kia ora, " + user + " this is a quiz created to test your maori language skills and New Zealand knowledge.")
answer = input ("Do you want to take this quiz? [yes/no] \n").lower()
if answer == "yes":
  q1()

  # https://www.youtube.com/watch?v=j1VkAGssvUg
else:
  print("Okay, maybe next time")
#ask question 1
