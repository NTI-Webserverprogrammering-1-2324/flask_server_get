from flask import Flask, render_template

app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    """Renders the index.html template.

    Returns:
        The rendered HTML template.
    """
    return render_template("index.html")

@app.route("/page")
def page():
    """Render the page.html template.

    Returns:
        The rendered page.html template.
    """
    return render_template("page.html")



@app.route("/hemsida")
def hemsida():
    """Returns a string containing the message "Här är min hemsida".

    Returns:
        str: A string containing the message "Här är min hemsida".
    """
    return "Här är min hemsida"


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


if __name__ == "__main__":
    app.run(debug=True, port=8000)
