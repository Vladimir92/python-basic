from flask import Flask, request, render_template

from homework9.views.product import product_app

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/ships")


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