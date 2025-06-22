import os
import requests
from flask import Blueprint, render_template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

modelo_bp = Blueprint("modelo", __name__)



@modelo_bp.route("/modelo")
def modelo():
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-ES&page=1"
    print(url)
    response = requests.get(url)
    datos = response.json()["results"]
    return render_template("cartelera.html", datos=datos)


