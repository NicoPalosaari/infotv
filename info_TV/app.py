from flask import Flask, jsonify, render_template, Response, current_app, g


from blueprints.helloworld.helloworld import helloworld_bp
from blueprints.calculator.calculator import calculator_bp
from blueprints.mediaplayer.mediaplayer import mediaplayer_bp
from blueprints.jokes.jokes import jokes_bp
from blueprints.weather.weather import weather_bp


app = Flask(__name__)
app.register_blueprint(helloworld_bp, url_prefix='/hello')
app.register_blueprint(calculator_bp, url_prefix='/calc')
app.register_blueprint(mediaplayer_bp)
app.register_blueprint(jokes_bp)
app.register_blueprint(weather_bp)


# Homepage
@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
