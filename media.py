class Movie():
    """Creates a data structure (i.e. Python Class) to store
    movies including movie titles, summaries, poster and trailer"""
    def __init__(self, movie_title, movie_summary, movie_poster, trailer_youtube):
        self.title = movie_title
        self.summary = movie_summary
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube
