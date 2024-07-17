#scissor paper rock game


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissor
'''

# Write your code below this line 👇
your_choice = int(input("please enter 0 for scissors,1 for paper and 2 for rock:"))
print("your choice is:")
computer_choice = random.randint(0, 2)

if your_choice==0:
    print(scissors)
elif your_choice==1:
    print(paper)
else:
    print(rock)

print("computer choice is:")
if computer_choice==0:
    print(scissors)
elif computer_choice == 1:
    print(paper)
else:
    print(rock)

if your_choice == computer_choice:
    print("draw")
elif your_choice == 0 and computer_choice == 1:
    print("you won")
elif your_choice ==2 and computer_choice == 0:
    print("you won")
elif your_choice ==1 and computer_choice == 2:
    print("you won")
else:
    print("you lose")







 
