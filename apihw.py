from flask import Flask, jsonify
import csv

app = Flask(__name__)

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

def read_data_from_csv(file_path, data_class):
    data_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            data = data_class(*row)
            data_list.append(data.__dict__)
    return data_list

@app.route('/movies')
def get_movies():
    file_path = 'movies.csv'  # ścieżka do pliku z danymi filmów
    movies = read_data_from_csv(file_path, Movie)
    return jsonify(movies)

@app.route('/links')
def get_links():
    file_path = 'links.csv'  # ścieżka do pliku z danymi links
    links = read_data_from_csv(file_path, Link)
    return jsonify(links)

@app.route('/ratings')
def get_ratings():
    file_path = 'ratings.csv'  # ścieżka do pliku z danymi ratings
    ratings = read_data_from_csv(file_path, Rating)
    return jsonify(ratings)

@app.route('/tags')
def get_tags():
    file_path = 'tags.csv'  # ścieżka do pliku z danymi tags
    tags = read_data_from_csv(file_path, Tag)
    return jsonify(tags)

if __name__ == '__main__':
    app.run(debug=True)