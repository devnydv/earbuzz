from flask import Flask, render_template
import json
#from flipkartgrid import senddata
#from flpkartp import detailsdata

app = Flask(__name__)
f = open("amazon.json", "rt")
#print(f.read())

data = json.load(f)
data = data['results']

@app.route("/")
def index():
    #data = senddata()
    return render_template("index.html", data= data)

@app.route("/products") 
def product():
    return render_template("products.html")

@app.route("/details") 
def details():
    #details = detailsdata()
    return render_template("details.html", data= details)


if __name__== "__main__":
    app.run(debug=True)