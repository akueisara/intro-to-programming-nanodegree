# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)

school_of_rock = media.Movie("School Of Rock", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight In Paris", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                "https://www.youtube.com/watch?v=mfmrPu43DF8")


your_name = media.Movie("Your Name",
                        "Two high school kids who've never met - city boy Taki and country girl Mitsuha - are united through their dreams.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
                        "https://www.youtube.com/watch?v=hRfHcp2GjVI")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

her = media.Movie("Her",
                  "A lonely writer develops an unlikely relationship with an operating system designed to meet his every need.",
                  "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

the_last_unicorn = media.Movie("The Last Unicorn",
                               "A brave unicorn and a magician fight an evil king who is obsessed with attempting to capture the world's unicorns.",
                               "https://upload.wikimedia.org/wikipedia/en/2/27/The_Last_Unicorn_%281982%29_theatrical_poster.jpg",
                               "https://www.youtube.com/watch?v=t-UpwWauZ50")

a_i_artificial_intelligence = media.Movie("A.I. Artificial Intelligence",
                                          "A highly advanced robotic boy longs to become \"real\" so that he can regain the love of his human mother.",
                                          "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
                                          "https://www.youtube.com/watch?v=_19pRsZRiz4")

bicentennial_man = media.Movie("Bicentennial Man",
                               "An android endeavors to become human as he gradually acquires emotions.",
                               "https://upload.wikimedia.org/wikipedia/en/f/fc/Bicentennial_man_film_poster.jpg",
                               "https://www.youtube.com/watch?v=nZ7HxlhVDyM")

movies = [your_name, interstellar, her, the_last_unicorn, a_i_artificial_intelligence, bicentennial_man]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
