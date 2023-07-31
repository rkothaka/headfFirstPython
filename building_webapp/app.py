from flask import Flask, render_template, request, Response
from vsearch import search4letters

app = Flask(__name__, template_folder='templates')


@app.route("/search_for", methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def page_entry():
    return render_template('entry.html',
                           the_title='Welcome to the web!')


if __name__ == '__main__':
    app.run(debug=True)
