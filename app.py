from flask import Flask, render_template
import json


app = Flask(__name__)
f = open("amazon.json", "r")
d = open("det.json", "r", encoding='utf-8' )

#print(f.read())

data = json.load(f)
data = data['results']
details = json.load(d)
pdetails = details['productDetails']


@app.route("/")
def index():
    #data = senddata()
    return render_template("index.html", data= data)

@app.route("/products") 
def product():
    return render_template("products.html")

@app.route("/details") 
def detail():
    #details = detailsdata()
    return render_template("details.html", data= pdetails, alld = details)

@app.route("/newdetails") 
def newdetail():
    #details = detailsdata()
    return render_template("detailsnew.html", data= pdetails, alld = details)


if __name__== "__main__":
    app.run(debug=True)