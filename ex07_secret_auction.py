# Ask the user for input
# Save data into dictionary {name: price}
# Ask if new bids need to be added
# Compare bids in dictionary


logo = r'''
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

print(logo)

bids_dict = {}
more_bids = True
while more_bids:
    name= input("What is your name? ")
    bid = int(input("What is your bid? EUR "))
    bids_dict[name] = bid
    carry_on = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    while carry_on != "yes" and carry_on != "no":
        print("Wrong input.\n")
        carry_on = input("Are there more bidders? Type 'yes' or 'no': ").lower()
    if carry_on == "no":
        more_bids = False
    elif carry_on == "yes":
        print('\n' * 50)

#Method1:
highest_value = 0
highest_bidder = ''
for bidder in bids_dict:
    if bids_dict[bidder] > highest_value:
        highest_value = bids_dict[bidder]
        highest_bidder = bidder
print(f"\nHighest bid was {bids_dict[highest_bidder]} EUR by {highest_bidder}.")

#Method2:
highest_bidder = (max(bids_dict, key=bids_dict.get))
print(f"\nHighest bid was {bids_dict[highest_bidder]} EUR by {highest_bidder}.")




