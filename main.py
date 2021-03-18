#initialize flask by importing flask
from flask import Flask 
app = Flask(__name__)
#python decorator "@app.route" that flask uses to connect URL endpoints with code contarinted in fucntions ("/" is the root path)
@app.route("/")
def index():#index is the convention
    # if user requests URL endpoint, run this code
    return "init complete" #this value will be shown to user
#start Flask's dev server when script is executed from cmd (not Google App Engine) so that u can run app from "py main.py"
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)