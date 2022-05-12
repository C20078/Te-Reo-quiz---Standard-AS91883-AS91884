# unit standard as91883 - as91884. Created by Charlotte Entwisle-Phillips, Started on 10/5/2022. My goal is to make a te reo quiz.
#https://replit.com/@Charlotte20078/test#main.py......https://replit.com/@reiman/Python-Challenge-The-Quiz#main.py

def q1():
  print ("Question 1")
  colour = input ("Whero is what color? Red / Green /  Orange / Blue = ")
  colour = colour.lower()
  if colour == "red":
    print ("Correct")
    q2()
  else:
    print ("Wrong")
    wrong()


def q2():
  print ("Question 2") 
  dance = input ("What is the traditional maori dance called? Pukana / Haka / Kabuki / Taki = ")
  dance = dance.lower()
  if dance == "haka":
    print ("Correct")
    q3()
  else:
    print ("Wrong")
    wrong()
  
def q3():
  print ("Question 3") 
  song = input("Fill in the blank for the song - One day a ____ went swimming in the moana. Taniwha / Mokopuna / Tuna = ")
  song = song.lower()
  if song == "taniwha":
    print ("Correct")
    q4()
  else:
    print ("wrong")
    wrong()
  
def q4():
  print ("Question 4") 
  ocean = input("What is the maori word for ocean?Wai / Moana = ")
  ocean = ocean.lower()
  if ocean == "moana":
    print ("Correct")
    q5()
  else:
    print ("Wrong")
    wrong()
  
def q5():
  print ("Question 5") 
  word = input ("Niu Tireni is the Māori word for New Zealand. False / True = ")
  word = word.lower()
  if word == "false":
    print ("Correct")
    correct()
  else:
    print ("Wrong")
    wrong()
    
  
def q6():
  print ("Question 6")
  store = input(" What would be stored in a Paataka? Pukapuka / Kai / Waka = ")
  store = store.lower()
  if input == "kai":
    print ("Correct")
    correct()
  else:
    print ("Wrong")
    wrong()

def wrong():
  print ("Sorry that answer was wrong")

def correct():
  print ("You got them all correct! Ka pai")
  print ("(っ◔◡◔)っ ♥ your amazing ♥")

print ("Te reo maori quiz - created by Charlotte ")
print ("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = input ("Hello, What is your name? ") 
print ("Ki ora, " + user + " this is a quiz created to test your maori language skills and New Zealand knowledge. There a 6 questions, Good luck! ")

q1()

