# Best player epl 2021 - 2022 season
# Create player class
from random import random, shuffle


class Player:
    # Create constructor with name,club,goal,assist,total
    def __init__(self, player_name: str, team: str, goal: int, assist: int, total: float):
        self.player_name = player_name
        self.team = team
        self.goal = goal
        self.assist = assist
        self.total = total
# Create total method based to goal + assist

    def total_points(self):
        self.total += self.goal + self.assist


# Create player object
mo_salah = Player("Mohamed salah", "liverpool", 23, 13, 0)
son_min = Player("Son min", "Spurs", 23, 7, 0)
kane = Player("Harry kane", "Spurs", 17, 9, 0)
bruyne = Player("Kevin", "Man city", 15, 8, 0)
bowen = Player("Jarrod bowen", "west ham", 12, 10, 0)


# Add player goal and assist by useing total_points method
mo_salah.total_points()
son_min.total_points()
kane.total_points()
bruyne.total_points()
bowen.total_points()

# Keep the object in a list
all_players = [ mo_salah,son_min, kane, bruyne, bowen,]
shuffle(all_players)
# Keep the total points in a list and find the largest one
points = [mo_salah.total, son_min.total, kane.total, bruyne.total, bowen.total]
points.sort()
best_player_points = points[len(points)-1]
print(best_player_points)

# Find the best player
for player in all_players:
    if player.total == best_player_points:
        print(f"{player.player_name} from {player.team} with goal:{player.goal},assist:{player.assist},total:{player.total} won the best player award.")
