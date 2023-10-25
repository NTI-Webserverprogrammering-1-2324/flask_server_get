"""
This is a Flask server that defines several routes that use the GET method.
"""

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
    """This function returns a string indicating that the page is private.

    Returns:
        str: A message indicating that the page is private.
    """
    return "This is a private page!"


@app.route("/user/<username>")
def user_message(username):
    """Return a welcome message for the given username.

    Args:
        username (str): The username to welcome.

    Returns:
        str: A welcome message for the given username.
    """
    return f"Welcome, {username}!"


@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    """Display the page for a specific post.

    Args:
        post_id (int): The ID of the post to display.

    Returns:
        str: A string containing the message to display on the page.
    """
    post_id_after = post_id + 1
    return f"This is the page for post # {post_id_after}."


@app.route("/profile/<username>")
def user_profile(username):
    """Render the user's profile page.

    Args:
        username (str): The username of the user whose profile page is being requested.

    Returns:
        str: The HTML content of the user's profile page.
    """
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
