from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('www', path)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    return 'done'


# If ran as a python script
if __name__ == "__main__":
    app.run('localhost', 8080)
