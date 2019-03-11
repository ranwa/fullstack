import webbrowser  # predifined library


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):  # init creates space in memory
        self.title = movie_title  # title of the movie
        self.storyline = movie_storyline  # storyline
        self.poster_image_url = poster_image  # url of the image
        self.trailer_youtube_url = trailer_youtube  # trailer link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
# open is a predefined function
