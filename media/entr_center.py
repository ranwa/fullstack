import media  # importing self created library
import fresh_tomatoes  # importing self created library

toy_story = media.Movie("toy story",
                        "a story of a boy and his toys that comes to life",
                        "https://goo.gl/yEimo9",
                        "https://www.youtube.com/watch?v=YImPH1hwhA4")
# toy_story is an instance of class movie and respective values are passed.
avatar = media.Movie("avatar",
                     "marine goes to alien planet",
                     "https://goo.gl/r81gRv",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
# avatar is an instance of class movie and respective values are passed.
school_of_rock = media.Movie("school of rock",
                             "using rock music to learn",
                             "https://goo.gl/Z9fQGV",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
# school of rock is an instance of class movie and respective values are passed
ratatouille = media.Movie("ratatouille",
                          "a rat is a chef in paris",
                          "https://goo.gl/DNHkYA",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
# ratatouille is an instance of class movie and respective values are passed.
midinght_in_paris = media.Movie("midnight in paris",
                                "going back in time to meet authors",
                                "https://goo.gl/r5Gz8w",
                                "https://www.youtube.com/watch?v=3wM06z5lA74")
# migdnight in paris is an instance of class movie and respective values are
# passed.
hunger_games = media.Movie("hunger games",
                           "a really real reality show",
                           "https://goo.gl/1YndNt",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")
# hunger games is an instance of class movie and respective values are passed.
movies = [toy_story, avatar, school_of_rock, ratatouille, midinght_in_paris,
          hunger_games]
# an array of name movies is defined
fresh_tomatoes.open_movies_page(movies)
# array is passed to fresh tomatoes
