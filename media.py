import webbrowser

class Video():
     """This class provides a way to store information common to Videos.
        It is a parent class for classes Movie & TvShow"""
     def __init__(self, name, title, duration, rating, poster_image_url, trailer_youtube_url):
        self.name = name
        self.title = title
        self.duration = duration
        self.rating = rating
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
     #common method to show the trailer of the video   
     def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)   
        
class Movie(Video):
    """This class provides a way to store movie specific information."""
    def __init__(self, name, title, movie_storyline, duration, rating, poster_image_url, trailer_youtube_url):
        Video.__init__(self, name, title, duration, rating, poster_image_url, trailer_youtube_url)
        self.storyline = movie_storyline
        
class TvShow(Video):
    """This class provides a way to store TV Show specific information."""
    def __init__(self, name, title, show_season, show_episode, show_tv_station,duration, rating, poster_image_url, trailer_youtube_url):
        Video.__init__(self, name, title, duration, rating, poster_image_url, trailer_youtube_url)
        self.season = show_season
        self.episode = show_episode
        self.tv_station = show_tv_station
        


