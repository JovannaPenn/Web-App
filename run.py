from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask (__name__)
app.secret_key = 'njwjfbo2948'

STARWARSDB= 'starwars.db'

@app.route('/')
def index():
    db = sqlite3.connect (STARWARSDB)
    print (db)
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    questions = []

    db = sqlite3.connect (STARWARSDB)
    print (db)

    cur = db.execute('SELECT * FROM questions')
    for row in cur:
        questions.append(row)

    db.close()

    return render_template('quiz.html', questions=questions)



@app.route('/result', methods=['POST'])
def result():
    db = sqlite3.connect (STARWARSDB)
    print (request.form)

    answer1 = request.form['1']
    answer2 = request.form['2']
    answer3 = request.form['3']

    if answer1=='1' and answer2=='1':
        result = 'The Phantom Menace, Attack of the Clones, Revenge of the Sith, Solo, Rogue One, A New Hope, The Empire Strikes back, Return of the Jedi, The Force Awakens, The Last Jedi'

    if answer1=='1' and answer2=='2':
        result = 'The Phantom Menace, Attack of the Clones, Revenge of the Sith, A New Hope, The Empire Strikes back, Return of the Jedi, The Force Awakens, The Last Jedi'

    if answer3=='2':
        result = 'A New Hope, The Phantom Menace, Attack of the Clones, Revenge of the Sith, The Empire Strikes Back, Return of the Jedi, The Force Awakens, The Last Jedi'

    if answer1=='3' and answer2=='3' and answer3=='3':
        result = 'A New Hope, The Empire Strikes Back, The Phantom Menace, Attack of the Clones, Revenge of the Sith, Return of the Jedi, The Force Awakens, The Last Jedi'

    if answer1=='3' and answer2=='1' and answer3=='3':
        result = 'A New Hope, Solo, Rogue One, The Empire Strikes Back, The Phantom Menace, Attack of the Clones, Revenge of the Sith, Return of the Jedi, The Force Awakens, The Last Jedi'

    if answer2=='2':
        result = 'A New Hope, The Phantom Menace, The Force Awakens, The Empire Strikes Back, Attack of the Clones, The Last Jedi, Return of the Jedi, Revenge of the Sith'

    if answer3=='1':
        result = 'A New Hope, The Empire Strikes Back, Return of the Jedi, The Phantom Menace, Attack of the Clones, Revenge of the Sith, The Force Awakens, Rogue One, The Last Jedi, Solo'


    SELECT COUNT(*) FROM results WHERE answer1 = 1 AND answer2 = 2 AND answer3 = 3;
    SELECT COUNT(*) FROM results;

    cur = db.execute(
    'INSERT INTO results(answer1, answer2, answer3) VALUES(?, ?, ?)',
    (answer1,answer2,answer3)
    )
    db.commit()
    db.close()


    return render_template('result.html', data=request.form, result=result)
