from flask import Flask, render_template,url_for
from flask_bootstrap import Bootstrap
from contentmanager import poster, links
app=Flask(__name__)
Bootstrap(app)
link=links()
posters=poster()
@app.route("/index")
def login():
   return render_template("index.html",posters=posters, link=link,)

@app.route("/admindashboard")
def admindashboard():
   return render_template("admindashboard.html")



if __name__ == "__main__":
    app.run(debug=True)
