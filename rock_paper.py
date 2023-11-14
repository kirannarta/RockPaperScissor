
# coding: utf-8

# In[49]:


## OrderedDict instead of dict
##import functions
import os
import random

rplay = random.choice(["rock", "paper", "scissors"])
hplay = input("Enter your choice  from rock, paper, scissors")

try:
    if hplay in ["rock", "paper", "scissors"]:
        if (rplay == "rock" and hplay == "paper") or (rplay == "paper" and hplay == "scissors") or (rplay == "scissors" and hplay == "rock"):
            print (f"I chose {rplay}; You win")
        elif (rplay == hplay):
            print (f"I also chose {rplay}; We Tie")
        else:
            print (f"I chose {rplay}; You Lose")
    else:        
        raise ValueError("Your input is incorrect")

except:
    print("wrong input, choose from rock, paper, scissors")
    