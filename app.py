from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello, GET!"


@app.route("/my/private/page")
def private():
    return "This is a private page!"


@app.route("/user/<username>")
def user_page(username):
    return f"Welcome, {username}!"


@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    post_id_after = post_id + 1
    return f"This is the page for post # {post_id_after}"


@app.route("/hemsida")
def hemsida():
    return "Här är min hemsida"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
