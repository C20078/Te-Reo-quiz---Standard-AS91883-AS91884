# unit standard as91883 - as91884. Created by Charlotte Entwisle-Phillips, Started on 10/5/2022. My goal is to make a te reo quiz.
#https://replit.com/@Charlotte20078/test#main.py......https://replit.com/@reiman/Python-Challenge-The-Quiz#main.py

def q1():
  print ("Question 1")
  colour = input ("Whero is what color? Red / Green /  Orange / Blue = ".lower())
  if colour == "red":
    print ("correct")
    q2()
  else:
    print ("wrong")
    wrong()


def q2():
  print ("this is question 2") 
  dance = input ("What is the traditional maori dance called? Pukana / Haka / Kabuki / Taki = ")
  if dance == "haka":
    print ("Correct")
    q3()
  else:
    print ("wrong")
    wrong()
  
def q3():
  print ("This is question 3") 
  song = input("Fill in the blank for the song - One day a ____ went swimming in the moana. Taniwha / Mokopuna / Tuna = ")
  if song == "taniwha":
    print ("Correct")
    q4()
  else:
    print ("wrong")
    wrong()
  
def q4():
  print ("This is question 4") 
  ocean = input("What is the maori word for ocean?Wai / Moana = ")
  if ocean == "moana":
    print ("Correct")
    q5()
  else:
    print ("wrong")
    wrong()
  
def q5():
  print ("This is question 5") 
  word = input ("Niu Tireni is the Māori word for New Zealand. False / True = ")
  if word == "false":
    print ("Correct")
    correct()
  else:
    print ("wrong")
    wrong()
    
  
def q6():
  print ("This is question 6")
  store = input(" What would be stored in a Paataka? Pukapuka / Kai / Waka = ")
  if input == "kai":
    print ("correct")
    correct()
  else:
    print ("wrong")
    wrong()

def wrong():
  print ("u suck")

def correct():
  print ("good job")

print ("hi this quiz")

user = input ("what is name ")
print ("hi " + user)
q1()

