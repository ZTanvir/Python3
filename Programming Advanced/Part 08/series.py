class Series:
    def __init__(self, title: str, season: int, genres: list):
        self.title = title
        self.season = season
        self.genres = genres
        self.total = []
        self.final_rate = ""
        self.rating = "no ratings"

    def rate(self, rating: int):
        self.total.append(rating)
        points = sum(self.total)
        total_user = len(self.total)
        avg = points / total_user
        self.final_rate = f"{avg:.1f}"
        if total_user > 0:
            self.rating = f"{total_user} ratings, average {avg:.1f} points"

    def __str__(self) -> str:
        genre_list = ", ".join(self.genres)
        return f"{self.title} ({self.season} seasons)\ngenres: {genre_list}\n{self.rating}"


def minimum_grade(rating: float, series_list: list):
    selected_series = []
    for series in series_list:
        series_rating = float(series.final_rate)
        if series_rating >= rating:
            selected_series.append(series)
    return selected_series


def includes_genre(genre: str, series_list: list):
    selected_seies = []
    for series in series_list:
        if genre in series.genres:
            selected_seies.append(series)
    return selected_seies


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
