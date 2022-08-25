from flask import Flask, render_template, request, flash   # import de l’objet Flask
import pandas as pd
def get_year(name):
	df_movies = pd.read_csv('/home/mathieu.vialat@Digital-Grenoble.local/Documents/drive/ML4/data/data/ml-latest-small/movies.csv')
	movie_title = df_movies[df_movies['title'].str.contains(name)]['title']
	print(movie_title.iloc[0][-6:])
	return movie_title.iloc[0][-6:]
	

app = Flask(__name__)  # instantiation application
title = ''
@app.route("/")
def home():
	return render_template('home.html')
@app.route("/form", methods=('GET', 'POST'))        # association d’une route (URL) avec la fonction ‘home()’
def form():
	global title
	if request.method == 'POST':
		title = request.form['filmname']
	#if not title:
	#	flash('Title is required!')
	return render_template('form.html')	
#@app.route("/Non")        # association d’une route (URL) avec la fonction ‘home()’
#def Non():
#	return render_template('Non.html')
#@app.route("/Sbradarajan")        # association d’une route (URL) avec la fonction ‘home()’
#def Sbradarajan():
#	return render_template('Sbradarajan.html')
@app.route("/about")        # association d’une route (URL) avec la fonction ‘home()’
def about(name = None, year = None):
	name = title or 'Unknown'
	year = get_year(title)
	return render_template('about.html', name=name, year=year)

app.run(host='127.0.0.9',port=4455,debug=True)   # démarrage de l’application







