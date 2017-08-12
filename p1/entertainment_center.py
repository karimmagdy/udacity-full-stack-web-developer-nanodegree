import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story" ,
                        "A story of a boy and his toys that come to life" ,
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" ,
                        "https://www.yo utube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar" ,
                        "A marine on an alien planet" ,
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg" ,
                        "https://www.youtube.com/watch?v=-9ceBgWV8io")
						
school_of_rock = media.Movie("School of Rock" ,
                        "Storyline" ,
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg" ,
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

avengers = media.Movie("Avengers: Age of Ultron" ,
                        "storyline" ,
                        "https://image.tmdb.org/t/p/w185/nveEFHidaEXZCG7zhfTc26hVqSu.jpg" ,
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")

mad_max = media.Movie("Mad Max: Fury Road" ,
                        "Storyline" ,
                        "https://image.tmdb.org/t/p/w185/oQoIl0j4Lk6NFvOA0u7UREF8Sxm.jpg" ,
                        "https://www.youtube.com/watch?v=cdLl1GVjOrc")

hunger_games = media.Movie("Hunger Games" ,
                        "Storyline" ,
                        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg" ,
                        "https://www.youtube.com/watch?v=PbA63a7H0bo")
						
the_hobbit = media.Movie("The Hobbit: The Battle of the Five Armies" ,
                        "Storyline" ,
                        "https://image.tmdb.org/t/p/w185/vgAHvS0bT3fpcpnJqT6uDTUsHTo.jpg" ,
                        "https://www.youtube.com/watch?v=iVAgTiBrrDA")
						
captain_america = media.Movie("Captain America: The Winter Soldier" ,
                        "Storyline" ,
                        "https://image.tmdb.org/t/p/w185/pH4oeiZAh9a40tly4D0l6aAB3ms.jpg" ,
                        "https://www.youtube.com/watch?v=7SlILk2WMTI")						

furious7 = media.Movie("Furious 7" ,
                        "Storyline" ,
                        "https://image.tmdb.org/t/p/w185/xTbSn1UHkyhY7BinfDQg83o3qjv.jpg" ,
                        "https://www.youtube.com/watch?v=5Yab0sXGEjg")						

movies = [avengers,mad_max,toy_story,avatar,school_of_rock,hunger_games,the_hobbit,captain_america,furious7]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
