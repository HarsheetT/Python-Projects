import random

computer_guess = random.choice(range(1,101))
print(computer_guess)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

# game_indicator = False

# while not game_indicator:
#     if difficulty_level == 'easy':
#         level = 10
#         print(f"You have {level} attempts remaining to guess the number!")
#         user_guess = input("Make a Guess!")

#         if user_guess == computer_guess:
#             print("You Win!")
#             game_indicator = True
#         elif user_guess > computer_guess:
#             print("Too High")
#         else:
#             print("Too Low")
#         level -= level
#         if level == 0:
#             print("Attempts Finished! You Lose.")
#             game_indicator = True

