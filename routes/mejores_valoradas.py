import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

mejores_valoradas_bp = Blueprint("mejores_valoradas", __name__)

@mejores_valoradas_bp.route("/mejores_valoradas")
def mejores_valoradas():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=es-ES&page=1"
    response = requests.get(url)
    if response.status_code != 200:
        return render_template("error.html", error="Error al obtener los datos de las películas.")
    datos = response.json()["results"]
    return render_template("mejores_valoradas.html", datos=datos)