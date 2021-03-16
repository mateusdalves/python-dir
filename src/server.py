from flask import Flask, render_template, request, url_for
import os
import conf
import main


root_dir = conf.Configuration.DIR

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/dir')
def list_dir():
    files = main.scan_dir(root_dir)
    return render_template('dir.html', files=files)



if __name__ == "__main__":
    app.run(debug=True)