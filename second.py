import keyword
name = input ("Hi I am Ai quizzes! What is your name?")
print ("Hello", name)
print ("How many continents are there in the world?", name)
print ("1. Eight ")
print ("2. 6")
print ("3. Seven")
Answer = input ("type in choice 1, 2 or 3!")

if Answer == "3":
    print ("Well done, you have completed the quest!")
else :
    print("Incorrect, better luck next time, redo the program to have a chance at winning!")
print (keyword.kwlist)