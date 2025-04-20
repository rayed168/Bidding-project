bidders = ["Ehtisham", "Usman", "Abdullah"]
players = {"Platinum": "Messi", "Gold": "Ronaldo", "Silver": "Neymar"}
bids = {"Messi": {}, "Ronaldo": {}, "Neymar": {}}

player_keywords = {
    "platinum": "Messi",
    "messi": "Messi",
    "gold": "Ronaldo",
    "ronaldo": "Ronaldo",
    "silver": "Neymar",
    "neymar": "Neymar"
}

while True:
    print("Players: Platinum - Messi, Gold - Ronaldo, Silver - Neymar")
    print("Bidders: Ehtisham, Usman, Abdullah")

    choices = {}
    for bidder in bidders:
        while True:
            choice_input = input(f"{bidder}, choose a player to bid on: ").strip().lower()
            words = choice_input.split()
            matched = None
            for word in words:
                if word in player_keywords:
                    matched = player_keywords[word]
                    break
            if matched:
                choices[bidder] = matched
                break
            else:
                print("Invalid input. Try something like 'gold', 'ronaldo', or 'Platinum Messi'.")

    player_groups = {}
    for bidder, player in choices.items():
        player_groups.setdefault(player, []).append(bidder)

    for player, group_bidders in player_groups.items():
        print(f"\nBidding on {player} by: {', '.join(group_bidders)}")
        for bidder in group_bidders:
            while True:
                try:
                    bid = int(input(f"{bidder}, enter your bid for {player}: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            bids[player][bidder] = bid

    print("\nAuction Results:")
    for player in players.values():
        if bids[player]:
            highest_bidder = max(bids[player], key=bids[player].get)
            highest_bid = bids[player][highest_bidder]
            print(f"{highest_bidder} wins the bid for {player} with ${highest_bid}.")

    break
