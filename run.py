from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask (__name__)

STARWARSDB= 'starwars.db'

questions = [
    ['Is this your first time watching the series?', 'It is my first time','I have seen 1 or 2', 'I have seen them all'],
    ['Would you want to include the prequels in your watching experience?', 'Yes', 'No', 'I do not mind'],
    ['What character would you want the movies to focus on?', 'Luke Skywalker', 'Obi-wan Kenobi', 'I do not mind']
]

@app.route('/')
def index():
    db = sqlite3.connect (STARWARSDB)
    print (db)
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    db = sqlite3.connect (STARWARSDB)
    print (db)
    return render_template('quiz.html', questions=questions)
