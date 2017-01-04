from flask import Flask, send_from_directory, render_template, request
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL
import csv
import datetime

app = Flask(__name__)


def writeToDB(reader):
    #initalize database connection and get cursor
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'expenses'
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()

    for row in reader:
        if isHeaderEntry(row): #skip header entries
            continue

        row[0] = datetime.datetime.strptime(str(row[0]), '%m/%d/%Y').strftime('%Y-%m-%d')
        query_string = 'INSERT INTO expenses VALUES (88, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'%tuple(row)
        cursor.execute(query_string)

    conn.commit()
    conn.close()

def isHeaderEntry(row):
    return row[0] == 'date'

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

    reader = csv.reader(f)

    try:
        writeToDB(reader)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (f.filename, reader.line_num, e))


    return render_template('upload.html')

# If ran as a python script
if __name__ == "__main__":
    app.run('localhost', 8080)
