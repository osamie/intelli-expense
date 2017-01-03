from flask import Flask, send_from_directory, render_template, request
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL
import csv

app = Flask(__name__)

def writeToDB(data):
    #initalize database connection
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'expenses'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()


    for row in data:
        query_string = 'INSERT INTO expenses VALUES (null, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");'

        cursor.execute(query_string, row)


    conn.commit()
    conn.close()



@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('www', path)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/uploadFile', methods=['POST'])
def upload():
    files = request.files

    # for key in files:
    f = files['0']
    print f.filename

    data = csv.reader(f)

    writeToDB(data)

    return render_template('upload.html')

# If ran as a python script
if __name__ == "__main__":
    app.run('localhost', 8080)
