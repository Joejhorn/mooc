class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.ratings_total = 0
        self.average = 0

    def __str__(self):
        genres = ', '.join(self.genres)
        if len(self.ratings) == 0:
            rating = 'no ratings'
            return (f'{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{rating}')
        else:

            rating = (f'{self.ratings_total} ratings, average {self.average:.1f} points ')
            genres = ', '.join(self.genres)

            return(f'{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{rating}')
    
    def rate(self, rating):
        self.ratings_total += 1
        self.ratings.append(rating)
        self.average = sum(self.ratings) / len(self.ratings)


# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# dexter.rate(4)
# dexter.rate(5)
# dexter.rate(5)
# dexter.rate(3)
# dexter.rate(0)
# print(dexter)

def minimum_grade(grade, list):
    movies = []
    for movie in list:
        if movie.average > grade:
            movies.append(movie)
    return movies
    
def includes_genre(genre, list):
    genres = []
    for movie in list:
        if genre in movie.genres:
            genres.append(movie)
    return genres

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




