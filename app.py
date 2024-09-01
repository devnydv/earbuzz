from flask import Flask, render_template, redirect, url_for
import json
from db import inddata, catdata

app = Flask(__name__)
f = open("amazon.json", "r")
d = open("det.json", "r", encoding='utf-8' )

#print(f.read())


details = json.load(d)
pdetails = details['productDetails']


@app.route("/")
def index():

    data = inddata()
    return render_template("index.html", data= data)

@app.route("/<cat>/") 
def product(cat):
    
    catd = catdata(cat)
    
    if catd != []:
        return render_template("products.html", data = catd )
    else:
        return redirect(url_for('error_404'))
        

@app.route("/details") 
def detail():
    #details = detailsdata()
    return render_template("details.html", data= pdetails, alld = details)

@app.route("/newdetails") 
def newdetail():
    #details = detailsdata()
    return render_template("detailsnew.html", data= pdetails, alld = details)

# Error handling




# Custom error pages
@app.route('/error_404')
def error_404():
    return render_template("error.html") , 404
    #return "This is a custom 404 error page.", 404


if __name__== "__main__":
    app.run(debug=True)