import fresh_tomatoes
import media
toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc""")
avtar = media.Movie("Avtar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8")
tiger = media.Movie("Tiger Zinda Hai",
                    "A story of indian and a pakistani spy",
                    "https://upload.wikimedia.org/wikipedia/en/5/5e/Tiger_Zinda_Hai_-_Poster.jpg",
                    "https://www.youtube.com/watch?v=ePO5M5DE01I")
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
fukrey_returns = media.Movie("Fukrey Returns",
                             "Story of 4 guys who dream big",
                             "https://upload.wikimedia.org/wikipedia/en/3/35/Fukrey_Returns.jpg",
                             "https://www.youtube.com/watch?v=f-UzOpuKOVY")
sultan = media.Movie("Sultan",
                     "Story based on a wrestler",
                     "https://upload.wikimedia.org/wikipedia/en/1/1f/Sultan_film_poster.jpg",
                     "https://www.youtube.com/watch?v=wPxqcq6Byq0")
movies = [toy_story, avtar, tiger, school_of_rock, fukrey_returns, sultan]
fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline);
#print(fukrey_returns.storyline);
#sultan.show_trailer();
