from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return '<%r %r %r %r %r>' %(self.username, self.email, self.firstname, self.lastname, self.password)

@app.route("/")
def main():
    print("route: /")
    return render_template("main.html")

@app.route("/index")
def index():
    print("route: /index")
    return render_template("index.html")

@app.route("/register", methods=['GET','POST'])
def register():
    print("route: /register")

    if request.method=='POST':
        email= request.form.get('email')
        username = request.form.get('username')
        password= request.form.get('password')
        fname= request.form.get('fname')
        lname= request.form.get('lname')

        user = User(
            email=email,
            username=username,
            password=password,
            firstname=fname,
            lastname=lname)
        
        id = db.session.add(user)
        db.session.commit()

        return("<h1>Successfully Saved Id: </h1>")
        
    return render_template("register.html")

@app.route("/login")
def login_page():
    print("route: /login")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
