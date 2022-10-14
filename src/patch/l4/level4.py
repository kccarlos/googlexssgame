from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def search():
    if not request.args.get('timer'):
        # Show main timer page
        return render_template('index.html')
    else:
        try:
            timer = int(request.args.get('timer'))
        except Exception as e:
            return render_template('index.html')
        return render_template('timer.html', timer=timer)

@app.route('/favicon.ico')
def send_icon():
    return send_from_directory(directory='static', path='favicon.ico')