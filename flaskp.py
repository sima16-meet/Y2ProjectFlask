from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home_page.html")

@app.route('/about')
def about():
	return render_template("about_me_page.html")

@app.route('/contact_me')
def contact():
	return render_template("contact_me.html")


if __name__ == "__main__": 
	app.run() 
