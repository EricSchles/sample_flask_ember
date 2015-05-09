from flask import Flask,jsonify,request
import json
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Create the Flask-SQLAlchemy object and an SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, unique=False)

    # When we create a new Todo it should be incomplete and have a title
    def __init__(self,data):
        self.data = data

@app.route("/api/test",methods=["GET","POST"])
@app.route("/api/test/<data>",methods=["GET","POST"])
def api_test(data=None):
    if request.method=='POST':
        print data
        if data:
            data=json.loads(data)
            info = Info(data['data'])
            db.session.add(info)
            db.session.commit()
            return "success"
    if request.method=='GET':
        return str(Info.query.all())
    
# Create the database tables.
db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
