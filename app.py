
from flask import Flask, render_template
#from flipkartgrid import senddata
from flpkartp import detailsdata
app = Flask(__name__)


@app.route("/")
def index():
    #data = senddata()
    #return render_template("index.html", data= data)
    return "lol"
@app.route("/products") 
def product():
    return render_template("products.html")

@app.route("/details") 
def details():
    details = detailsdata()
    return render_template("details.html", data= details)
   # return "lol"

#if __name__== "__main__":
 #   app.run(debug=True)
