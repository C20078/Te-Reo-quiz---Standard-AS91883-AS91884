score = 0
# unit standard as91883 - as91884. Created by Charlotte Entwisle-Phillips, Started on 10/5/2022. My goal is to make a te reo quiz.
#https://replit.com/@Charlotte20078/test#main.py......https://replit.com/@reiman/Python-Challenge-The-Quiz#main.py

#purpose of code is to create a quiz while being funtional and good/easy to understand

#this part of code should send them to q2 or wrong depending on input v6
#this is gonna make my work look *FABULOUS* (greens my favorite colour)

def q1():
  print ("\n"
         "Question 1")
  colour = input ("Whero is red [true/false] \n")
  colour = colour.lower()
  if colour == "true":
    print ("Correct")
    q2()
    score =+ 1 

  else:
    print ("Wrong")
    q2()
    score =- 1
    
  
    
#ask question 2, this part of code should send them to q3 or wrong depending on input v3
def q2():
  print ("\n"
         "Question 2") 
  dance = input ("the traditonal maori dance is Pukana [true/false] \n" )
  dance = dance.lower()
  if dance == "false":
    print ("Correct")
    q3()
    
  else:
    print ("Wrong")
    q3()

#ask question 3, this part of code should send them to q4 or wrong depending on input v3
def q3():
  print ("\n"
         "Question 3") 
  song = input("tahi is 10 in maori [true/false] \n")
  song = song.lower()
  if song == "false":
    print ("Correct")
    q4()
 
  else:
    print ("Wrong")
#ask question 4, this part of code should send them to q5 or wrong depending on input  v3
def q4():
  print ("\n"
  "Question 4") 
  ocean = input("moana is the maori word for ocean? [true/false]\n")
  ocean = ocean.lower()
  if ocean == "true":
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
#this is gonna make my work look *FABULOUS* 
print("\033[1;35m ")
#this is the intro, welcome the user explain the quiz. this is version3. dates edited/made 9/5/22 11/5/22 12/5/22
print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = input ("Hello, What is your name? ") 
print ("Kia ora, " + user + " this is a quiz created to test your maori language skills and New Zealand knowledge.")
answer = input ("Do you want to take this quiz? [yes/no] \n").lower()
if answer == "yes":
  q1()
  print (score)

  # https://www.youtube.com/watch?v=j1VkAGssvUg
else:
  print("Okay, maybe next time")
#ask question 1
