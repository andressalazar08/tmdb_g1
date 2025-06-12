import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

mejoresvaloradas_bp = Blueprint("mejores_valoradas", __name__)

@mejoresvaloradas_bp.route("/mejores_valoradas")
def mejores_valoradas():
    datos=[]
    for page in range (1,4):
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=es-ESpage={page}"
        response = requests.get(url)
        datos.extend (response.json()["results"])
    return render_template("mejores_valoradas.html", datos=datos)