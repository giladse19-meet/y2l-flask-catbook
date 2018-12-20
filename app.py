from flask import Flask
from flask import render_template, request
from database import get_all_cats
from database import get_cat_by_id
from database import add_vote
from database import create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>', methods=['GET', 'POST'])
def cats_route(id):
    cat = get_cat_by_id(id)
    if request.method == "GET":
        return render_template(
            'cat.html', cat=cat)
    else:
        add_vote(cat.id)
        return render_template(
            'cat.html', cat=cat)

@app.route('/add_cat', methods=['GET', 'POST'])
def add_cat():
    if request.method == "GET":
        return render_template('add-cat.html')
    else:
        name = request.form['catname']
        create_cat(name=name, vote=0)
        return render_template('add-cat.html')

if __name__ == '__main__':
   app.run(debug = True)
