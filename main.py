from flask import Flask, Blueprint
from routes.popular import popular_bp
from routes.elencoyequipos import credits_bp
import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
app.register_blueprint(popular_bp)
app.register_blueprint(credits_bp)

if __name__=="__main__":
    app.run(debug=True)