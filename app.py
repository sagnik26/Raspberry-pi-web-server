from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,template_folder="template")
app.secret_key="bfvjfhbvjfbfhdbc@$#43fmj76fhjfnfhbvfvjvvmvfm"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db"
db=SQLAlchemy(app)

class Devices(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    api_name = db.Column(db.String(30),nullable=False)
    state = db.Column(db.String(10),nullable=False)
    disp_name = db.Column(db.String(30),nullable=False)


db.create_all()

@app.route("/control panel")

def index():
    return render_template("temp.html")

@app.route("/myname/<name>")

def ret_name(name):
    return "your name is "+name



if __name__=="__main__":
    app.run(debug=True)






