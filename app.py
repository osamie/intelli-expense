from flask import Flask, send_from_directory, render_template, request
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL

app = Flask(__name__)

def testDbConnection():
    #initalize database connection
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'expenses'
    mysql.init_app(app)

    conn = mysql.connect()

    cursor = conn.cursor()

    query_string = 'SELECT * FROM expenses'
    cursor.execute(query_string)
    data = cursor.fetchall()
    print data[0]
    conn.close()



@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('www', path)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/uploadFile', methods=['POST'])
def upload():
    f = request.files['the_file']
    f.save('/var/www/uploads/' + secure_filename(f.filename))
    print f
    return render_template('upload.html')

# If ran as a python script
if __name__ == "__main__":
    app.run('localhost', 8080)
