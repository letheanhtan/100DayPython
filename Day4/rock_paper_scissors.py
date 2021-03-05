import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
listChoices = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"Your choice\n{listChoices[your_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer choice\n{listChoices[computer_choice]}")

if your_choice == computer_choice:
    print("It is a draw")
else:
    if your_choice == 0 and computer_choice == 1:
        print("You lose")
    elif your_choice == 0 and computer_choice == 2:
        print("You win")
    elif your_choice == 1 and computer_choice == 0:
        print("You win")
    elif your_choice == 1 and computer_choice == 2:
        print("You lose")
    elif your_choice == 2 and computer_choice == 0:
        print("You lose")
    else:
        print("You lose")
