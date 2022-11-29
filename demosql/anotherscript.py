#!/user/bin/env python3

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/students")
def roster():

    conn = sqlite3.connect('school.db')
    cursor = conn.execute('SELECT * from STUDENT')

    rows = []
    for x in cursor:
        emptydict = {"StudentID": x[0], "Name": x[1], "GPA": x[2], "Age": x[3]}
        rows.append(emptydict)
    return rows


#Add a route that allows POSTed new students to be added to the database!

#add a route that allows PUTs to change student values

#Add a route that DELTES students (graduate/expelled)

if __name__ == "__main__":
    app.run(hosts="0.0.0.0", port=2224)
