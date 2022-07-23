class Series:
    def __init__(self, title: str, season: int, genres: list):
        self.title = title
        self.season = season
        self.genres = genres
        self.total = []
        self.rating = "no ratings"

    def rate(self, rating: int):
        self.total.append(rating)
        points = sum(self.total)
        total_user = len(self.total)
        avg = points / total_user
        if total_user > 0:
            self.rating = f"{total_user} ratings, average {avg:.1f} points"

    def __str__(self) -> str:
        genre_list = ", ".join(self.genres)
        return f"{self.title} ({self.season} seasons)\ngenres: {genre_list}\n{self.rating}"


dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)
