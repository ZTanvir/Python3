# Best player epl 2021 - 2022 season
# Create player class
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