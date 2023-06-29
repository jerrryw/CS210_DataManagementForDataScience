# --- PART 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    ratingsDict = {}
    for line in f:
        movie, rating, ids = line.strip().split('|')
        rating = float(rating)
        if (movie in ratingsDict):
            ratingsDict[movie].append(rating)
        else:
            ratingsDict[movie] = [rating]
    # print(ratingsDict)
    return ratingsDict

# 1.2
def read_movie_genre(f):
    movieGenreDict = {}
    for line in f:
        genre, ids, movie = line.strip().split('|')
        if (movie in movieGenreDict):
            movieGenreDict[movie].append(genre)
        else:
            movieGenreDict[movie] = [genre]
    # print(movieGenreDict)
    return movieGenreDict

# --- PART 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    genreDict = {}
    for movie, genres in d.items():
        for genre in genres:
            if (genre in genreDict):
                genreDict[genre].append(movie)
            else:
                genreDict[genre] = [movie]
    # print(genreDict)
    return genreDict

# 2.2
def calculate_average_rating(d):
    avgRatingDict = {}
    for movie, ratings in d.items():
        avgRatingDict[movie] = round((sum(ratings) / len(ratings)), 2)
    # print(avgRatingDict)
    return avgRatingDict

# --- PART 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    sortedMovies = sorted(d.items(), key = lambda x : x[1], reverse = True)

    if (len(sortedMovies) <= n):
        # print(dict(sortedMovies))
        return(dict(sortedMovies))

    nMovies = dict(sortedMovies[:n])
    # print(nMovies)
    return nMovies

# 3.2
def filter_movies(d, thres_rating=3):
    filterRatingDict = {}
    for movie, rating in d.items():
        if (rating >= thres_rating):
            filterRatingDict[movie] = rating
    # print(filterRatingDict)
    return filterRatingDict

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    moviesInGenre  = genre_to_movies[genre]
    averageRating  = {movies: movie_to_average_rating[movies] for movies in moviesInGenre}
    sortByRatings  = sorted(averageRating.items(), key = lambda x: x[1], reverse = True)
    nMovies        = sortByRatings[:n]
    popularInGenre = {movie: avg_rating for movie, avg_rating in nMovies}
    # print(popularInGenre)
    return popularInGenre

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    movieInGenre = genre_to_movies.get(genre, [])
    # print(movieInGenre)
    sumRating = 0
    numMovies = 0
    for movie in movieInGenre:
        rating    = movie_to_average_rating.get(movie, 0)
        sumRating += rating
        numMovies += 1
    if (numMovies > 0):
        averageRating = sumRating / numMovies
        # print(averageRating)
        return averageRating

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genreRatings = {}
    for genre, movies in genre_to_movies.items():
        genreRatings[genre] = round(get_genre_rating(genre, genre_to_movies, movie_to_average_rating), 2)
    sortByRatings = sorted(genreRatings.items(), key = lambda x: x[1], reverse = True)

    if (len(sortByRatings) > n):
        # print(dict(sortByRatings[:n]))
        return dict(sortByRatings[:n])
    else:
        # print(dict(sortByRatings))
        return dict(sortByRatings)

# --- PART 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    userToMoviesDict = {}
    for line in f:
        movie, rating, ids = line.strip().split('|')
        if (ids not in userToMoviesDict):
            userToMoviesDict[ids] = []
        userToMoviesDict[ids].append((movie, rating))
    # print(userToMoviesDict)
    return userToMoviesDict

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    genreRatings = {}
    if (user_id in user_to_movies):
        movies = user_to_movies[user_id]
        for movie, rating in movies:
            if (movie in movie_to_genre):
                genre   = movie_to_genre[movie]
                t_genre = tuple(genre)
                if (t_genre not in genreRatings):
                    genreRatings[t_genre] = []
                genreRatings[t_genre].append(float(rating))

        if (len(genreRatings) > 0):
            averageRatings = {}
            for genre, ratings in genreRatings.items():
                averageRatings[genre] = sum(ratings) / len(ratings)
            # print(max(averageRatings))
            return max(averageRatings)

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    userRatedMovies = set([movie for movie, rating in user_to_movies[user_id]])
    # print("userRatedMovies:", userRatedMovies)
    userTopGenre    = get_user_genre(user_id, user_to_movies, movie_to_genre)
    # print("userTopGenre:", userTopGenre)
    topMovies       = [movie for movie, genres in movie_to_genre.items() if userTopGenre in genres and movie not in userRatedMovies]
    # print("topMovies:", topMovies)
    topGenreRatings = {movie: rating for movie, rating in movie_to_average_rating.items() if movie in topMovies}
    # print("topGenreRatings:", topGenreRatings)
    recommendMovies = sorted(topGenreRatings.items(), key = lambda x: x[1], reverse = True)[:3]
    # print(dict(recommendMovies))
    return dict(recommendMovies)