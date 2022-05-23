# unit standard as91883 - as91884. Created by Charlotte Entwisle-Phillips, Started on 10/5/2022. My goal is to make a te reo quiz.
#https://replit.com/@Charlotte20078/test#main.py......https://replit.com/@reiman/Python-Challenge-The-Quiz#main.py

#purpose of code is to create a quiz while being funtional and good/easy to understand

#this part of code should send them to q2 or wrong depending on input v6
#this is gonna make my work look *FABULOUS* (greens my favorite colour)
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
    print ("correct")
    q2()
  elif colour == "c":
    print ("correct")
    q2()
  else:
    print ("Wrong")
    wrong()
    
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
    print ("correct")
    q3()
  elif dance == "b":
    print ("correct")
    q3()
  else:
    print ("Wrong")
    wrong()

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
    print ("correct")
    q4()
  elif song == "a":
    print ("correct")
    q4()
  else:
    print ("Wrong")
    wrong()
    
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
    print ("correct")
    q5()
  elif ocean == "b":
    print ("correct")
    q5()
  else:
    print ("Wrong")
    wrong()

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
    print ("correct")
    q6()
  elif word == "b":
    print ("correct")
    q6()
  else:
    print ("Wrong")
    wrong()
    
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
    print ("correct")
    correct()
  elif store == "b":
    print ("correct")
    correct()
  else:
    print ("Wrong")
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

  

#this is gonna make my work look *FABULOUS* 
print("\033[1;36m ")
#this is the intro, welcome the user explain the quiz. this is version3. dates edited/made 9/5/22 11/5/22 12/5/22
print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = input ("Hello, What is your name? ") 
print ("Kia ora, " + user + " this is a quiz created to test your maori language skills and New Zealand knowledge. There a 6 questions, please type in the answers form the options listed. Good luck! ")

#ask question 1
q1()

