from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = "Новый проект"
        return render_template('index.html')
    

    @app.route('/about')
    def about():
        title = "О нас"
        return render_template('about.html')

    return app