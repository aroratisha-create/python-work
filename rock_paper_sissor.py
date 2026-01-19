import random 
user=input("ENER YOUR CHOICE!! IF U DARE....")
possible_actions=["rock","paper","sissors"]
computer_actions=random.choice(possible_actions)
print(f"YOUR CHOICE!!{user},computer choice{computer_actions}")
if user==computer_actions:
    print("DRAWW!NO ONE WINS SO LETS PLAY AGAIN!")
elif user=="rock":
    if computer_actions=="sissors":
        print("WELL DONE THIS TIME! NEXT TIME U WILL REGRET U WON...!")
    else:print("I WIN! MUHAHAHAHAHA!!")
elif user=="sissors":
    if computer_actions=="paper":
        print("WELL DONE THIS TIME! NEXT TIME U WILL REGRET U WON...!")
    else:print("I WIN! MUHAHAHAHAHA!!")
elif user=="paper":
    if computer_actions=="sissors":
        print("WELL DONE THIS TIME! NEXT TIME U WILL REGRET U WON...!")
    else:print("I WIN! MUHAHAHAHAHA!!")

