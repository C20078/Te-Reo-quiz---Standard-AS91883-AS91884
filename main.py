score = 0
# unit standard as91883 - as91884. Created by Charlotte Entwisle-Phillips, Started on 10/5/2022. My goal is to make a te reo quiz.
#https://replit.com/@Charlotte20078/test#main.py......https://replit.com/@reiman/Python-Challenge-The-Quiz#main.py

#purpose of code is to create a quiz while being funtional and good/easy to understand

#this part of code should send them to q2 or wrong depending on input v6
#this is gonna make my work look *FABULOUS* (greens my favorite colour)

def q1():
  global score
  print ("\n"
         "Question 1")
  colour = input ("Whero is red [true/false] \n")
  colour = colour.lower()
  if colour == "true":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q2()
 
  elif colour == "false":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q2()

  elif colour == "t":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q2()

  elif colour == "f":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q2()

  else:
    print("Please try with either True / false")
    q1()
  
#ask question 2, this part of code should send them to q3 or wrong depending on input v3
def q2():
  global score
  print ("\n"
         "Question 2") 
  dance = input ("the traditonal maori dance is Pukana [true/false] \n" )
  dance = dance.lower()
  if dance == "false":
    score +=1 
    print ("correct")
    print ("your score = ")
    print (score)
    q3()
    
    
  elif dance == "true":
    score -=1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q3()

  elif dance == "f":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q3()

  elif dance == "t":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q3()

  else:
    print("Please try with either True / false")
    q2()
  
#ask question 3, this part of code should send them to q4 or wrong depending on input v3
def q3():
  global score
  print ("\n"
         "Question 3") 
  song = input("tahi is 10 in maori [true/false] \n")
  song = song.lower()
  if song == "false":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q4()
    
  elif song == "true":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q4()

  elif song == "f":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q4()

  elif song == "t":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q4()
  
  else:
    print("Please try with either True / false")
    q3()
  
#ask question 4, this part of code should send them to q5 or wrong depending on input  v3
def q4():
  global score
  print ("\n"
  "Question 4") 
  ocean = input("moana is the maori word for ocean? [true/false]\n")
  ocean = ocean.lower()
  if ocean == "true":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q5()
    
  elif ocean == "false":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q5()

  elif ocean == "t":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q5()

  elif ocean == "f":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q5()

  else:
    print("Please try with either True / false")
    q4()
    
#ask question 5, this part of code should send them to q6 or wrong depending on input v3
def q5():
  global score
  print ("\n"
  "Question 5") 
  word = input ("Niu Tireni is the Māori word for New Zealand [true/false] \n")
  word = word.lower()
  if word == "false":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q6()
     
  elif word == "false":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q6()

  elif word == "f":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    q6()

  elif word == "t":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    q6()

  else:
    print("Please try with either True / false")
    q5()
    
#ask question 6, this part of code should send them to correct or wrong depending on input v4
def q6():
  global score
  print ("\n"
  "Question 6")
  store = input("kai would be stored in a Paataka? [true/false]\n")
  store = store.lower()
  if store == "true":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    results()

  elif store == "false":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    results()

  elif store == "t":
    score +=1 
    print ("Correct")
    print ("your score = ")
    print (score)
    results()

  elif store == "f":
    score -= 1
    print ("Wrong")
    print ("your score = ")
    print (score)
    results()
    
  else:
    print("Please try with either True / false")
    q6()

#if all answers are answered v7
def results():
  print()
  print ("Your over all score is ")
  print (score)
  print ("You did well " + user + "\n"
         "(っ◔◡◔)っ ♥ you're amazing ♥ \n")

#IDK WTF IM DOINGGGGGGGGGGGGGGGGG
#this is gonna make my work look *FABULOUS* 
print("\033[3;31m ")
#this is the intro, welcome the user explain the quiz. this is version3. dates edited/made 9/5/22 11/5/22 12/5/22
print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = input ("Hello, What is your name? ") 
print ("Kia ora, " + user + " this is a quiz created to test your maori language skills and New Zealand knowledge.")

answer = input ("Do you want to take this quiz? [yes/no] \n").lower()

if answer == "yes":
  q1()

else:
  print ("Okay, maybe next time")

  # https://www.youtube.com/watch?v=j1VkAGssvUg
