import art

print(art.logo)

continue_bid = "yes"
bid_dict = {}
max_bid = 0
max_name = ""

while continue_bid == 'yes':
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    bid_dict[name] = bid

    # TODO-3: Whether if new bids need to be added
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if continue_bid == 'yes':
        print("\n " * 100)

    # TODO-4: Compare bids in dictionary
    if bid > max_bid:
        max_bid = bid
        max_name = name

print(f"The winner is {max_name} with a bid of ${max_bid}")