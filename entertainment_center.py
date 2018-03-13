import fresh_tomatoes
import media

#defining each movie with the correct parameters set
toy_story = media.Movie("toy_story",
                        "Toy Story",
                        "A story of a boy and his toys coming to life",
                        "95 mins",
                        "",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("avatar",
                     "Avatar",
                     "A marine on an alien planet.",
                     "90mins",
                     "",
                     "https://vignette.wikia.nocookie.net/jamescameronsavatar/images/6/6c/Avatar_Poster.jpg/revision/latest?cb=20100105110229",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

persuit_happyness = media.Movie("persuit",
                                "The Pursuit of Happyness",
                                "Entrepreneur Chris Gardner's nearly one-year struggle being homeless",
                                "100 mins",
                                "",
                                "http://www.impawards.com/2006/posters/pursuit_of_happyness.jpg",
                                "https://www.youtube.com/watch?v=89Kq8SDyvfg");

ratatouille = media.Movie("ratatouille",
                          "Ratatouille",
                          "Remy, a rat, aspires to become a renowned French chef."
                          "He doesn't realise that people despise rodents and will never enjoy a meal cooked by him.",
                          "85 mins",
                          "",
                          "https://vignette.wikia.nocookie.net/disney/images/c/c8/Ratatouille_poster.jpg/revision/latest?cb=20130328084644",
                          "https://www.youtube.com/watch?v=ALUmKa_mpik");

angry_bird = media.Movie("angry",
                         "The Angry Birds",
                         "Red, Chuck and Bomb have always been the outcasts within a community of flightless birds on an island."
                         "But when mysterious green pigs intrude the island, it's up to them to figure out the reason.",
                         "80 mins",
                         "",
                         "http://www.impawards.com/2016/posters/angry_birds.jpg",
                         "https://www.youtube.com/watch?v=QRmKa7vvct4");

spiderman  = media.Movie("spiderman",
                         "Spider-Man",
                         "Peter Parker, a shy high school student, is often bullied by people."
                         "His life changes when he is bitten by a genetically altered spider and gains superpowers.",
                         "100 mins",
                         "",
                         "http://www.impawards.com/2002/posters/spiderman_ver1.jpg",
                         "https://www.youtube.com/watch?v=O7zvehDxttM");

#defining each tv show with the correct parameters set
seinfeld  = media.TvShow("seinfeld",
                         "SeinFeld",
                         "Season 1",
                         "Episode 1",
                         "ABC",
                         "60 mins",
                         "",
                         "http://www.gstatic.com/tv/thumb/tvbanners/7892827/p7892827_b_v8_aa.jpg",
                         "https://www.youtube.com/watch?v=dHh_ddv-dBE");

breaking_bad  = media.TvShow("breaking_bad",
                             "Breaking Bad",
                             "Season 5",
                             "Episode 8",
                             "ABC",
                             "45 mins",
                             "",
                             "https://vignette.wikia.nocookie.net/breakingbad/images/a/af/Season_4_Poster_3.jpg",
                             "https://www.youtube.com/watch?v=HhesaQXLuRY");

#list of movies to be shown
movies = [toy_story,avatar, persuit_happyness, ratatouille, angry_bird, spiderman]

#list of tv shows to be shown
tv_shows = [seinfeld, breaking_bad]

# calling the open page to generate the HTML
fresh_tomatoes.open_movies_page(movies,tv_shows)
