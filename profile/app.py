from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def base():
        """Our about us page."""
        return render_template('base.html')


    return app