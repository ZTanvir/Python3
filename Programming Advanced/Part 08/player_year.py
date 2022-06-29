from datetime import date


class PlayerYear:
    def __init__(self,player,day,month,year,points):
        # Default value 
        self.player = ""
        self.date_of_py = date(1900,1,1)
        self.points = 0

        if self.name_ok(player):
            self.player = player

        if self.date_ok(day,month,year):
            self.date_of_py = date(year,month,day)

        if self.points_ok(points):
            self.points = points

    def name_ok(self,name):
        return len(name) >= 2
    
    def date_ok(self,day,month,year):
        try:
            date(year,month,day)
            return True
        except:
            return False

    def points_ok(self,points):
        return points >= 0


mane_player = PlayerYear("mane",10,5,2022,100)
print(mane_player.player)
print(mane_player.date_of_py)
print(mane_player.points)

