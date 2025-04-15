bidders = ["Ehtisham", "Usman", "Abdullah"]
players = {"Platinum": "Messi", "Gold": "Ronaldo", "Silver": "Neymar"}
bids = {"Messi": {}, "Ronaldo": {}, "Neymar": {}}

while True:
    print("Players: Platinum - Messi, Gold - Ronaldo, Silver - Neymar")
    print("Bidders: Ehtisham, Usman, Abdullah")
    choices = {}
    for bidder in bidders:
        choice = input(f"{bidder}, choose a player to bid on: ")
    if choice not in players.values():
        print("Invalid player. Try again.")
        continue
    if bidders[0] == bidders[1] and bidders[0] == bidders[2]:
        print("All bidders have not chosen the same player. Try again.")
        continue
    agreed_players = {}
    for bidder in bidders:
        agreed_player = input(f"{bidder}, choose a player to bid on: ")
        while agreed_player not in players.values():
            print("Invalid player. Try again.")
            agreed_player = list(choices.values())[0]
        agreed_players[bidder] = agreed_player

    for bidder, agreed_player in agreed_players.items():
        bid = int(input(f"{bidder}, enter your bid for {agreed_player}: "))
        bids[agreed_player][bidder] = bid

    for player in players.values():
        if bids[player]:
            highest_bidder = max(bids[player], key=bids[player].get)
            highest_bid = bids[player][highest_bidder]
            print(f"{highest_bidder} wins the bid for {player} with ${highest_bid}.")