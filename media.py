import webbrowser

# Author: Brian Roy
# Date: Feb. 8, 2015
# Version: 1 
# Revision History: None
class Movie():
	"""The Movie() class is used to store information about movies.  It stores the movies title, storeline, box office poster, and trailer"""
	def __init__(self, movie_title, movie_storyline, movie_image, movie_trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_image
		self.trailer_youtube_url = movie_trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)