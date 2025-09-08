# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list[str]):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings_count = 0
        self.rating = 0

    def rate(self, rating: int):
        self.ratings_count += 1
        self.rating += rating

    def ratings_string(self):
        average = self.rating / self.ratings_count
        return f'{self.ratings_count} ratings, average {average:.1f} points'
    
    def __str__(self):
        return f'{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{'no ratings' if self.ratings_count == 0 else self.ratings_string()}'
    
def minimum_grade(rating: float, series_list: list):
    at_least_grade = [series for series in series_list if series.rating >= rating]
    return at_least_grade

def includes_genre(genre: str, series_list: list):
    includes_genre_list = [series for series in series_list if genre in series.genres]
    return includes_genre_list
