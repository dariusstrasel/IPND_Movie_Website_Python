import webbrowser


class Video():
    def __init__(self, title, storyline, poster_url, author, year):
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.author = author
        self.year = year


class Movie(Video):
    def __init__(self, title, storyline, poster_url, author, year, trailer_youtube):
        Video.__init__(self, title, storyline, poster_url, author, year)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)