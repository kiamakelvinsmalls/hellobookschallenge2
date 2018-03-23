from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app=Flask(__name__)
Bootstrap(app)

@app.route("/index")
def login():
   return render_template("index.html")

if __name__ == "main__":
	app.run(debug=True)
