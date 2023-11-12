import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from forms import CreateMovieForm


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    """
    Show the home page
    """
    return "<h1>This is Home Page</h1>"


@app.route('/movies/')
def movies_list():
    """
    Show the list of movies from db
    """

    # this is for test
    movies = {'1': {'name': 'The Killer', 'year': '2023'},
              '2': {'name': 'Rumble Through the Dark', 'year': '2023'},
              '3': {'name': 'Outlaw Johnny Black', 'year': '2023'},
              '4': {'name': 'Death on the Border', 'year': '2023'},
              '5': {'name': 'Oppenheimer', 'year': '2023'}}
    return jsonify(movies)


@app.route('/movies/add/', methods=['GET', 'POST'])
def create_movie():
    """Create movie with form"""

    form = CreateMovieForm()

    if request.method == 'POST' and form.validate_on_submit():
        title = request.form['title'].strip()
        year = request.form['year']
        return jsonify({'title': title, 'year': year})
    else:
        return render_template('create_movie.html', form=form)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
