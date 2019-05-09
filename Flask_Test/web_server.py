from flask import Flask, render_template

from Flask_Test.plot.figure_plot import Plotter

web_app = Flask(__name__)


@web_app.route('/home')
def home():
    plotter = Plotter()
    # draw figures
    plotter.bar_plot('sentiment_distribution', 'test_db')

    return render_template("index.html")


if __name__ == '__main__':
    web_app.run(host="localhost", port=5000, debug=True)