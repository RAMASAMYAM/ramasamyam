print('welcome to general quiz')

player = input('do you want to play? (yes/no):  ')

if player.lower() != "yes":
      quit()

print('ok lets play')
score=0 

# Question 1
print("1. Who is known as the father of computer science?")

print("a. Charles Babbage")
print("b. Alan Turing")
print("c. Ada Lovelace")
print("d. John von Neumann")

question = input("Your answer (a/b/c/d: ").strip().lower()
if question.lower() == "b":
          print('correct')
          score +=1
else:
         print('incorrect. The correct answer is b. Alan Turing.')

# Question 2      
print("2. Which element has the atomic number 1?")

print("a. Helium")
print("b. Lithium")
print("c. Hydrogen")
print("d. Beryllium")

question = input("Your answer (a/b/c/d:  ").strip().lower()
if question.lower() == "c":
          print('correct')
          score +=1   
else:
         print('incorrect. The correct answer is c. Hydrogen')

#Question 3      
print("3. Who won the 2024 T20 World Cup?")

print("a. Australia")
print("b. Pakistan")
print("c. England")
print("d. India")

question = input("Your answer (a/b/c/d: ").strip().lower()
if question.lower() == "d":
          print('correct')
          score +=1
else:
         print('incorrect. The correct answer is d. India')

# Question 4
print("4. Which country is known as the Land of the Rising Sun?")

print("a. China")
print("b. Japan")
print("c. South Korea")
print("d. Thailand")

question = input("Your answer (a/b/c/d: ").strip().lower()
if question.lower() == "b":
           print('correct')
           score +=1
else:
           print('incorrect. The correct answer is b. Japan')

# Question 5
print("5. What is the capital city of Australia?")

print("a. Canberra")
print("b. Melbourne")
print("c. Sydney")
print("d. Brisbane")

question = input("Your answer (a/b/c/d: ").strip().lower()
if question.lower() == "a":
           print('correct')
           score +=1
else:
        print('incorrect. the corect answer is a. Canberra')

print(f"your final score : {score} out of 5")
