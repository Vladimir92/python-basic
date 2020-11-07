from flask import Flask, request, render_template
from flask_migrate import Migrate

import config
from views import product_app
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)
app.register_blueprint(product_app, url_prefix="/ships")

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/", methods=["GET", "POST"])
def index():
    title = "ship showdown"
    name = "Vlad"
    if request.method == "POST":
        name = request.form.get('name', 'Vlad')
    return render_template("index.html", name=name, page_title=title)


@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    if name is None:
        name = "World"
    return f"<h1>Hello {name}!</h1>"


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post int %d' % post_id