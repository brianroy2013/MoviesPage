import media
import fresh_tomatoes

# Create a list of milves
toy_story = media.Movie("Toy Story",
						"A story abou a bou and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
					 "A marine on a alien planet",
					 "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

iron_man = media.Movie("Iron Man",
	             "The creation of a new super hero",
	             "http://upload.wikimedia.org/wikipedia/en/e/e0/Iron_Man_bleeding_edge.jpg",
	             "https://www.youtube.com/watch?v=8hYlB38asDY")

thor2 = media.Movie("Thor 2",
	                "The sequal to Thor",
	                "http://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
	                "https://www.youtube.com/watch?v=-hwGggrQL2g")

avengers = media.Movie("Avengers",
	                   "Avengers",
	                   "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
	                   "https://www.youtube.com/watch?v=MZoO8QVMxkk")

hunger_games = media.Movie("Hunger Games",
	                       "Hunger Games",
	                       "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
	                       "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story,avatar,iron_man,thor2,avengers,hunger_games]

# The fresh_tomatoes.open_movies_page(movies) function takes a list of movies and converts into a html page (file name:"fresh_tomatoes.html")
# This function was provided by Udacity.com
fresh_tomatoes.open_movies_page(movies)