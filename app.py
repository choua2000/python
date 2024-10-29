
from flask import Flask,render_template

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret key"

from router.routes import *
# from router.userRoute import *


if __name__ == "__main__":
    app.run(debug=True, port='3000')


    
