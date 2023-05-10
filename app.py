from flask import *
import requests as r
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/urldm")
def ud():
    return render_template("urlcode.html")
@app.route("/wycode=<url>")
def uc(url):
    new_url="http://"+url
    rs = r.get(new_url).text
    print(rs)
    return rs
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)