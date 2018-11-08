from flask import Flask
from flask import render_template
from database import get_all_cats
from database import get_cat_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cats_route(id):
    cat = get_cat_by_id(id)
    return render_template(
        'cat.html', cat=cat)

if __name__ == '__main__':
   app.run(debug = True)
