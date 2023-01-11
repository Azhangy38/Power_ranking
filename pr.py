# the display option I chose, feel free to experiment with other displays
from prettytable import PrettyTable

pt = PrettyTable()


# Duelist class
class Duelist:
    def __init__(self, name, wins, losses, draws, decks, invites):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.decks = decks
        self.invites = invites

    def getWinRate(self):
        if self.wins + self.losses > 0:
            win_rate = self.wins / (self.wins + self.losses)
        else:
            win_rate = 0
        return win_rate

    def getPR(self):
        if self.getWinRate() > 0:
            pr = (self.wins * 100 - self.losses * 50 + self.draws * 25 + self.invites * 600) * (self.getWinRate())
        elif self.invites > 0 and self.losses == 0:
            pr = self.invites * 600;
        else:
            pr = (self.Wins * 100 - self.losses * 50 + self.draws * 25)
        return pr


# adjustable based on what you are trying to rank
pt.field_names = ['Rank', 'Player', 'Deck(s)', 'W', 'L', 'D', 'Win%', 'Invites (non-OTS)', 'PR']
Power_Rank = []

# add more players as necessary
player1 = Duelist('Player_Name1', 1, 0, 0, 'Deck', 1)
player2 = Duelist('Player_Name2', 2, 0, 0, 'Deck', 1)

# added to the array of players
Power_Rank.append(player1)
Power_Rank.append(player2)

# player_sort(Power_Rank)
sorted(Power_Rank, key=lambda p: p.getPR())

rank = 1
for duelist in Power_Rank:
    pt.add_row([rank, duelist.name, duelist.decks, duelist.wins, duelist.losses, duelist.draws, duelist.getWinRate() *
                100, duelist.invites, duelist.getPR()])
    rank = rank + 1
print(pt)
