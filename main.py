import os
from datetime import datetime
from flask import Flask, render_template, url_for, redirect, send_from_directory, abort, request
    
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(64)
app.config['SERVER_NAME'] = 'localhost:5000'

@app.route("/")
def index():
    return render_template('index.html', year=datetime.now().year)

@app.route("/about")
def about():
    return render_template('about.html', year=datetime.now().year)

# portfolios
@app.route("/graphic-design")
def graphicdesign():
    return render_template('ProtfolioGraphicsDesign.html', year=datetime.now().year)

@app.route("/3d")
def renders():
    return render_template('Portfolio3D.html', year=datetime.now().year)

@app.route("/film")
def film():
    return render_template('PortfolioFilm.html', year=datetime.now().year)


# --------------------------------------
#                 Errors
# --------------------------------------
# 400 Bad Request.
@app.errorhandler(400)
def error404(error):
    return render_template('Errors.html', Error="400", message="Bad Request")
# 401 Unauthorized.
@app.errorhandler(401)
def error404(error):
    return render_template('Errors.html', Error="401", message="Unauthorized Access Error")
# 404 Page not found.
@app.errorhandler(404)
def error404(error):
    return render_template('Errors.html', Error="404", message="Page not found")
# 403 You dont have permission.
@app.errorhandler(403)
def error403(error):
    return render_template('Errors.html', Error="403", message="You don't have permission to access this part of the website.")
# Too many requests
@app.errorhandler(429)
def error404(error):
    return render_template('Errors.html', Error="429", message="Too many requests Error")
# 500 Internal Server Error
@app.errorhandler(500)
def error500(error):
    return render_template('Errors.html', Error="500", message="Internal Server Error")
# 502 Bad Gateway.
@app.errorhandler(502)
def error500(error):
    return render_template('Errors.html', Error="502", message="Bad Gateway")
# 503 Service Unavailable.
@app.errorhandler(503)
def error500(error):
    return render_template('Errors.html', Error="503", message="Service Unavailable")
# 504 Gateway Timeout.
@app.errorhandler(504)
def error504(error):
    return render_template('Errors.html', Error="504", message="Gateway Timeout")

if __name__ == "__main__":
    app.debug = False
    app.run(threaded=True)