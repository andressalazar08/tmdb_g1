from flask import Flask, Blueprint 

from routes.popular import popular_bp

from routes.genero_de_peliculas import genero_de_peliculas_bp #inporto

import os

from dotenv import load_dotenv


load_dotenv()


app=Flask(__name__)

app.register_blueprint(popular_bp)

app.register_blueprint(genero_de_peliculas_bp)







if __name__=="__main__":
    app.run(debug=True)