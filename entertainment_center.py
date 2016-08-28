import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
                        "Pixar Animation Studios",
                        "1995",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


spirited_away = media.Movie("Spirited Away",
                            "Chihiro Ogino, a sullen ten-year-old girl who, while moving to "
                                             "a new neighborhood, enters the spirit world.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Spirited_Away_poster.JPG/220px-Spirited_Away_poster.JPG",
                            "Hayao Miyazaki",
                            "2008",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

shawshank = media.Movie("The Shawshank Redemption",
                            "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                            "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                            "Frank Darabont",
                            "1994",
                            "https://www.youtube.com/watch?v=6hB3S9bIaco")

pulp = media.Movie("Pulp Fiction",
                            "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                            "http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "Quentin Tarantino",
                            "1994",
                            "https://www.youtube.com/watch?v=wZBfmBvvotE")

inception = media.Movie("Inception",
                            "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                            "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "Christopher Nolan",
                            "2010",
                            "https://www.youtube.com/watch?v=66TuSJo4dZM")

matrix = media.Movie("The Matrix",
                            "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                            "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "The Wachowski Brothers",
                            "1999",
                            "https://www.youtube.com/watch?v=m8e-FF8MsqU")

cog = media.Movie("City of God",
                            "Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.",
                            "http://ia.media-imdb.com/images/M/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "Fernando Meirelles, Katia Lund",
                            "2002",
                            "https://www.youtube.com/watch?v=ioUE_5wpg_E")

interstellar = media.Movie("Interstellar",
                            "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                            "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "Christopher Nolan",
                            "2014",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA")

tgm = media.Movie("The Green Mile",
                            "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.",
                            "http://ia.media-imdb.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "Frank Darabont",
                            "1999",
                            "https://www.youtube.com/watch?v=uDybmxbKf4Y")



movies = [toy_story, spirited_away, shawshank, pulp, inception, matrix, cog, interstellar, tgm]
fresh_tomatoes.open_movies_page(movies)