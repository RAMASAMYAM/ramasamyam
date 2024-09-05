print('welcome to general quiz')

player = input('do you want to play? ')

if player.lower() != "yes":
      quit()

print('ok lets play')
score=0 

question = input("who is known as the father of computer science? ")
if question.lower() == "alan turing":
          print('correct')
          score +=1
else:
         print('incorrect')
      
      
question = input("which element has the atomic number 1? ")
if question.lower() == "hydrogen":
          print('correct')
          score +=1   
else:
         print('incorrect')
      

question = input("who won 2024 t20 world cup? ")
if question.lower() == "india":
          print('correct')
          score +=1
else:
         print('incorrect')

question = input("which country is known as the land of the rising sun?")
if question.lower() == "japan":
           print('correct')
           score +=1
else:
           print('incorrect')

question = input("what is the capital city of australia?")
if question.lower() == "canberra":
           print('correct')
           score +=1
else:
        print('incorrect')

print("your score " + str(score))
