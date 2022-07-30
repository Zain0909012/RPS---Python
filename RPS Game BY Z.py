#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Simple RPS Game (Rock Paper Scissor Game Using Python)
import random
userwin=0
compwin=0
options=["rock","paper","scissor"]

while True:
    userinput=input("Type Rock or Paper or Scissor or Q for Quit Game: ").lower()
    if userinput=="q":
        print("\nThanks for Playing Z's Game")
        break
        
    if userinput not in options:
        continue
    #for computer    
    random_number=random.randint(0,2)
    # scissor=0 ,rock=1,paper=2
    
    computer_input=options[random_number]
    print("Computer Picked",computer_input)
    
    
    if userinput=="rock" and computer_input=="scissor":
        userwin +=1
        print("YOu Won")
        
    elif userinput=="paper" and computer_input=="rock":
        userwin +=1
        print("YOu Won")  
        
    elif userinput=="scissor" and computer_input=="paper":
        userwin +=1
        print("YOu Won")   
        
    else:
        compwin+=1
        print("You lost")

print("You Wins",userwin,"times")
print("Computer Wins",compwin,"times")


# In[ ]:


Q

