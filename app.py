from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/home")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)