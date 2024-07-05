import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear_output():
    if os.name == 'nt':
        os.system('cls') #For Windows
    else:
        os.system('clear') #For Linux

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")

print(logo)

bids = {}

bidding_finish = False
while not bidding_finish:
    name = input("What is your name? ")
    price = int(input("What is your bid? ₹ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or no: ").lower()
    if should_continue == 'no':
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear_output()

