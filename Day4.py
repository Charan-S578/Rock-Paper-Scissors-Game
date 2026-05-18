import random
#random_integer = random.randint(1, 10)
#print(random_integer)
#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)
#random_float = random.uniform(1, 10)
#print(random_float)
#random_heads_or_tails = random.randint(a=0, b=1)
#if random_heads_or_tails == 0:
#    print("Heads")
#else:
#    print("tails")    

#states_of_india = ["Karnataka", "Andhra Pradesh", "Telanagana", "TamilNadu"]   
#states_of_india[3] = "Madras"
#states_of_india.pop(1)
#print(states_of_india)

#friends = ["Charan", "Rahul", "Hemanth", "Moksha"]
#print(random.choice(friends))
#random_index = random.randint(a=0, b=4)
#print(friends[random_index])

#south_india_heros = ["Ram Charan", "Pawan Kalyan", "Prabhas", "Mahesh Babu", "Jr NTR", "Allu Arjun", "Vijay", "Surya", "Rajanikanth", "Kamal Hassan", "Dhanush"]
#tollywood_heros = ["Ram Charan", "Pawan Kalyan", "Prabhas", "Mahesh Babu", "Jr NTR", "Allu Arjun"]
#kallywood_heros = ["Vijay", "Surya", "Rajanikanth", "Kamal Hassan", "Dhanush"]
#south_india_heros = [tollywood_heros, kallywood_heros]
#print(south_india_heros)

# Day 4 Project Rock, Paper, Sessiors

import random

rock = '''_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = ''' _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
sessiors = '''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, sessiors]

user_choice = (input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors \n"))
print(game_images[user_choice])

computer_choice = random.randint(a=0, b=2)
print("Computer choose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number. You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")   
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")  
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")  
elif computer_choice == user_choice:
    print("It's a draw!")             