import webbrowser


class Video():
    """Parent class of Movie. Used to hold high-;evel attributes which all media may share. The child, Movie inherits
    a number of said attributes."""
    def __init__(self, title, storyline, poster_url, author, year):
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.author = author
        self.year = year


class Movie(Video):
    """Movie it the primary class object for passing meta-data to the HTML/CSS generator. This also holds the class
    method for opening the YouTube url on the final site."""
    def __init__(self, title, storyline, poster_url, author, year, trailer_youtube):
        Video.__init__(self, title, storyline, poster_url, author, year)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)