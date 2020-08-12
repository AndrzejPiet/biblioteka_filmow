class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        # Variables
        self.views = 0


    def play(self, watch = 1):
        self.views += watch
        
    def __str__(self):
        return f'{self.title} {self.year} '    


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        self.season = season
        self.episode = episode

    def play(self, watch = 1):
        self.views += watch

    def __str__(self):
        return f"{self.title} - {self.season}{self.episode}"