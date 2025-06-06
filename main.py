from flask import Flask, Blueprint
from routes.mejores_valoradas import mejoresvaloradas_bp
import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)
app.register_blueprint(mejoresvaloradas_bp)

if __name__=="__main__":
    app.run(debug=True)