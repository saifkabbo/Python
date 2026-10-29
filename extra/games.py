# import random
# def get_choice():
#     player_choice=input("Enter your choice: rock, paper, scissors\n")
#     options=["rock","paper","scissors"]
#     computer_choice=random.choice(options)
#     choose={"player":player_choice,"computer":computer_choice}   
#     return choose

# def get_result(player,computer):
#     if player==computer:
#         return "It's a tie."
#     elif player=="rock" and computer=="scissors":
#         return "Rock smashes scissor, YOU WIN"
#     elif player=="scissor" and computer=="rock":
#         return "Rock smaches scissors, YOU LOSS"
#     elif player=="paper" and computer=="scissors":
#         return "Scissors cuts paper, YOU LOSS"
#     elif player=="scissors" and computer=="paper":
#         return "Scissors cuts paper, YOU WIN"
#     elif player=="rock" and computer=="paper":
#         return "Paper cover rock, YOU LOSS"
#     elif player=="paper" and computer=="rock":
#         return "Paper cover rock, YOU WIN"
#     else:
#         return "Try Again"

# choose=get_choice()
# result=get_result(choose["player"],choose["computer"])
# print(choose)
# print(result) 